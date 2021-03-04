from django.urls import path
from Accounts import views
urlpatterns = [
    # path('register/', auth_views., name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),


]