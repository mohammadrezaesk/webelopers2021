from django.urls import path, include
from Panel import views
urlpatterns = [
    path('', views.panel, name="panel"),


]