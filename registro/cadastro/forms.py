from django import forms

from .models import Uf, Municipio, Medico, Doencas

class PacienteForm(forms.Form):

  def get_lista_uf():
    lista = Uf.objects.values_list('sigla', 'nome')
    return lista

  def get_lista_municipios():
    lista = Municipio.objects.values_list('id', 'nome')
    return lista

  def get_lista_medicos():
    lista = Medico.objects.values_list('id', 'nome')
    return lista

  def get_lista_doencas():
    lista = Doencas.objects.values_list('id', 'nome')
    return lista

  nome  = forms.CharField(label="Nome", max_length=200, required=True)
  data_nascimento = forms.DateField(label="Data de nascimento", required=True, widget=forms.SelectDateWidget(years=range(1900, 2021)))
  doenca = forms.ChoiceField(label="Comorbidade", choices=get_lista_doencas(), required=False)
  data_diagnostico = forms.DateField(label="Data de diagnóstico", required=False, widget=forms.SelectDateWidget(years=range(1900, 2021)))
  descricao_doenca = forms.CharField(label="Descrição da doença", required=False, widget=forms.Textarea)
  medico = forms.ChoiceField(label="Médico responsável", choices=get_lista_medicos(), required=False)
  sexo = forms.ChoiceField(label="Sexo", choices=[('M', 'M'), ('F', 'F')], required=False)
  nome_mae  = forms.CharField(label="Nome da mãe", max_length=200, required=True)
  estado = forms.ChoiceField(label="Estado", choices=get_lista_uf(), required=False)
  municipio = forms.ChoiceField(label="Municipio", choices=get_lista_municipios(), required=False)
  login  = forms.CharField(label="Usuário", max_length=200, required=True)
  senha  = forms.CharField(label="Senha", max_length=200, required=True, widget=forms.PasswordInput)