from django.urls import path, include
from Panel import views
urlpatterns = [
    path('', views.panel, name="panel"),
    path('new/', views.create_product, name="create_product"),
    path('myproducts/', views.my_products, name="my_products"),



]