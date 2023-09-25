from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Hospital, Medico, Paciente, Cita, Consulta, Receta


# Base view
class HomeView(ListView):
    model = Hospital
    template_name = 'base.html'

# Hospital Views
class HospitalListView(ListView):
    model = Hospital
    template_name = 'hospital_list.html'

class HospitalCreateView(CreateView):
    model = Hospital
    fields = ['nombre', 'direccion', 'telefono', 'email']
    success_url = reverse_lazy('hospital_list')
    
class HospitalUpdateView(UpdateView):
    model = Hospital
    fields = ['nombre', 'direccion', 'telefono', 'email']
    success_url = reverse_lazy('hospital_list')
    
class HospitalDeleteView(DeleteView):
    model = Hospital
    success_url = reverse_lazy('hospital_list')


# Medico Views
class MedicoListView(ListView):
    model = Medico
    template_name = 'medic_list.html'

class MedicoCreateView(CreateView):
    model = Medico
    fields = ['nombre', 'apellido', 'telefono', 'email', 'hospital']
    success_url = reverse_lazy('medic_list')

class MedicoUpdateView(UpdateView):
    model = Medico
    fields = ['nombre', 'apellido', 'telefono', 'email', 'hospital']
    success_url = reverse_lazy('medic_list')

class MedicoDeleteView(DeleteView):
    model = Medico
    success_url = reverse_lazy('medic_list')

