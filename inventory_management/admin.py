from django.contrib import admin
from .models import Material, InventoryMovement, Category, Supplier, Units

admin.site.register(Material)
admin.site.register(InventoryMovement)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Units)

# Register your models here.
