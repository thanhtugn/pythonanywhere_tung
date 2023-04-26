from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^login/', views.login, name='login'),
    re_path(r'^logout/', views.logout, name='logout'),
    re_path(r'^signup/', views.signup, name='signup'),
]

