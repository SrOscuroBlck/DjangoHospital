"""
URL configuration for SysMed project.

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

from Hospital.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),

    # Hospital URLs
    path('hospitales/', HospitalListView.as_view(), name='hospital_list'),
    path('hospital/new/', HospitalCreateView.as_view(), name='hospital_form'),
    path('hospital/edit/<int:pk>/', HospitalUpdateView.as_view(), name='hospital_edit'),
    path('hospital/delete/<int:pk>/', HospitalDeleteView.as_view(), name='hospital_delete'),

    # Medico URLs
    path('medicos/', MedicoListView.as_view(), name='medic_list'),
    path('medico/new/', MedicoCreateView.as_view(), name='medic_form'),
    path('medico/edit/<int:pk>/', MedicoUpdateView.as_view(), name='medic_edit'),
    path('medico/delete/<int:pk>/', MedicoDeleteView.as_view(), name='medic_delete'),
]
