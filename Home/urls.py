from django.contrib import admin
from django.urls import path, include
from Home import views
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('contactus/', views.contactus, name="contactus"),
    path('all_products/', views.all_products, name="all_products"),
    path('search_products/', views.all_products, name="search_products"),
    path('submit_rate/<int:prd_id>', views.submit_rate, name="submit_rate"),
    path('product/<int:prd_id>', views.product_page, name="product_page"),
    path('comment/<int:prd_id>', views.write_comment, name="write_comment"),


]