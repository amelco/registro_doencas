from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from datetime import date, datetime

from .models import Pacientes, Login, Tipo_usuario, Uf, Municipio, Doencas, Medico
from .forms import PacienteForm

def index(request):
  return render(request, 'cadastro/index.html')

def paciente(request):
  if request.method == 'POST':
    form = PacienteForm(request.POST)
    if form.is_valid():
      paciente = form.cleaned_data
      l = Login()
      l.login = paciente['login']
      if Login.objects.filter(login = l.login).exists():
        return render(request, 'cadastro/error.html', {'message': 'Usuário já existe', 'origin': 'paciente'})
      l.senha = make_password(paciente['senha'])
      l.Tipo_usuario_id = Tipo_usuario.objects.get(tipo = "Paciente")
      l.save()
      p = Pacientes()
      p.nome = paciente['nome']
      if Pacientes.objects.filter(nome = p.nome).exists():
        return render(request, 'cadastro/error.html', {'message': 'Paciente já existe'})
      born = paciente['data_nascimento']
      today = date.today()
      age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
      p.idade = age
      p.data_nascimento = paciente['data_nascimento']
      p.data_diagnostico = paciente['data_diagnostico']
      p.descricao_doenca = paciente['descricao_doenca']
      p.nome_mae = paciente['nome_mae']
      p.sexo = paciente['sexo']
      p.uf_id = Uf.objects.get(sigla = paciente['estado'])
      p.Municipio_id = Municipio.objects.get(id = paciente['municipio'])
      p.Login_id = Login.objects.get(login = paciente['login'])
      p.Doencas_id = Doencas.objects.get(id = paciente['doenca'])
      p.Medico_id = Medico.objects.get(id = paciente['medico'])
      p.save()
      return HttpResponse("Usuario cadastrado")
  else:
    form = PacienteForm()
  
  return render(request, 'cadastro/paciente.html', {'form': form})

def medico(request):
  return HttpResponse("Página de medicos")

def gestor(request):
  return HttpResponse("Página de gestores")

def gestor_lista_pacientes(request):
  pacients = Pacientes.objects.order_by('nome')
  # output = ', '.join([p.nome for p in pacients])
  context = {
    'pacients': pacients
  }
  return render(request, 'cadastro/index.html', context)
