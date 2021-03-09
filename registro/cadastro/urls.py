from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('paciente/', views.paciente, name="paciente"),
  path('medico/', views.medico, name="medico"),
  path('gestor/', views.gestor, name="gestor"),
  path('gestor/lista_pacientes', views.gestor_lista_pacientes, name="gestor_lista_pacientes")
]