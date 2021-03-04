from django.urls import path, include
from Panel import views
urlpatterns = [
    path('', views.panel, name="panel"),
    path('new/', views.create_product, name="create_product"),
    path('my_products/', views.my_products, name="my_products"),
    path('edit_product/<int:prd_id>/', views.edit_product, name="edit_product"),



]