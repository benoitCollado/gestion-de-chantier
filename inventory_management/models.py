from django.db import models
from django.db.models.deletion import DO_NOTHING

class Category(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()

  def __str__(self):
    return self.name

class Supplier(models.Model):
  name = models.CharField(max_length=100)
  siret = models.CharField(max_length=14)
  street_nummder = models.CharField(max_length=100)
  street_name = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  postal_code = models.CharField(max_length=5)
  country = models.CharField(max_length=100)
  contact_person = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  email = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Units(models.Model):
  name = models.CharField(max_length=100)
  code = models.CharField(max_length=5)

  def __str__(self):
    return self.code
  

class Material(models.Model):
  name = models.CharField(max_length=100)
  code = models.CharField(max_length=100)
  description = models.TextField()
  category_id = models.ForeignKey(Category, on_delete=DO_NOTHING)
  supplier_id = models.ForeignKey(Supplier, on_delete=DO_NOTHING)
  reorder_level = models.IntegerField()
  unit_id = models.ForeignKey(Units, on_delete=DO_NOTHING)

  def __str__(self):
    return self.name

class InventoryMovement(models.Model):
  material_id = models.ForeignKey(Material, on_delete=DO_NOTHING)
  quantity = models.IntegerField()
  movement_type = models.CharField(max_length=100)
  movement_date = models.DateField()
  note = models.TextField()

  def __str__(self):
    return f"{self.material_id.name} - quantity :{self.quantity} - date : {self.movement_date} - type : {self.movement_type}"


# Create your models here.
