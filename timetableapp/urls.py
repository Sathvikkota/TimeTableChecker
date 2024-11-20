from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='user_login'),
    path('adminhome/', views.admin_home, name='admin_home'),
    path('filter/<clash_type>',views.filterByclash,name="filterByclash"),
]

