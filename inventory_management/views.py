from django.db.models.expressions import OrderBy
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Material, InventoryMovement, Category, Supplier, Units

def index(request):
    materials = Material.objects.select_related(
      'category_id',
      'supplier_id'
    ).order_by('name')[:10]
    #materials = Material.objects.all().order_by('name')[:10]
    categories = Category.objects.all().order_by('name')[:10]
    supliers = Supplier.objects.all().order_by('name')[:10]
      
    context = {
      "materials" : materials,
      "categories" : categories,
      "suppliers" : supliers
    }
    return render(request, 'inventory/index.html', context)

def materialList(request):
    materials = Material.objects.select_related(
      'category_id',
      'supplier_id'
    ).order_by('name')[:10]

    context = {
      "materials" : materials
    }
    return render(request, 'inventory/materialList.html', context)

def materialCreate(request):
    if request.method == 'POST' : 
      #print(request.POST)
      print("avant")
      category = Category.objects.filter(id = request.POST['category_id'])
      print(category[0])
      supplier = Supplier.objects.filter(id = request.POST['supplier_id'])
      unit = Units.objects.filter(id = request.POST['unit_id'])
      material = Material.objects.create(
        name = request.POST['name'],
        code = request.POST['code'],
        description = request.POST['description'],
        category_id = category[0],
        supplier_id = supplier[0],
        reorder_level = int(request.POST['reorder_level']),
        unit_id = unit[0]
      )
      print('après')
      material.save()
      print('ok modif')
      return HttpResponseRedirect(reverse('inventory:materialList'))
        
    else : 
      suppliers = Supplier.objects.all().order_by('name')
      categories = Category.objects.all().order_by('name')
      units = Units.objects.all().order_by('name')
      context = {
        "suppliers" : suppliers,
        "categories" : categories,
        "units" : units
      }
      
      return render(request, 'inventory/materialCreate.html', context)

  


# Create your views here.
