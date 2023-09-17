"""
URL configuration for animals project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('animals/', views.animals_list, name='animals_list'),
    path('families/', views.families_list, name='families_list'),
    path('animal/<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('animal_in_family/<int:family_id>/', views.animals_in_family, name='animals_in_family'),
    path('song', views.create_children_song, name='create_children_song'),
]