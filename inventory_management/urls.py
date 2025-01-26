from django.urls import path

from . import views
app_name = 'inventory'
urlpatterns =[
  path("", views.index, name="index"),
  path("materialList", views.materialList, name="materialList"),
  path("materialCreate", views.materialCreate, name="materialCreate"),
]