from django.db import models

class Doencas(models.Model):
  nome = models.CharField(max_length=200)

  def __str__(self):
    return self.nome

class Uf(models.Model):
  sigla = models.CharField(max_length=2)
  nome = models.CharField(max_length=50)

  def __str__(self):
    return self.sigla

class Municipio(models.Model):
  nome = models.CharField(max_length=100)
  Uf_id = models.ForeignKey(Uf, on_delete=models.CASCADE)

  def __str__(self):
    return self.nome

class Tipo_usuario(models.Model):
  tipo = models.CharField(max_length=50)

  def __str__(self):
    return self.tipo

class Login(models.Model):
  login = models.CharField(max_length=50)
  senha = models.CharField(max_length=255)
  Tipo_usuario_id = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE)

  def __str__(self):
    return self.login

class Medico(models.Model):
  nome = models.CharField(max_length=200)
  crm = models.CharField(max_length=50)
  Login_id = models.ForeignKey(Login, on_delete=models.CASCADE)

  def __str__(self):
    return self.nome + " " + self.crm

class Gestor(models.Model):
  nome = models.CharField(max_length=200)
  Login_id = models.ForeignKey(Login, on_delete=models.CASCADE)

  def __str__(self):
    return self.nome

class Pacientes(models.Model):
  nome = models.CharField(max_length=200)
  idade = models.SmallIntegerField()
  data_nascimento = models.DateField(auto_now=False, auto_now_add=False)
  data_diagnostico = models.DateField(auto_now=False, auto_now_add=False, default=None, blank=True, null=True)
  descricao_doenca = models.TextField(default=None, blank=True, null=True)
  nome_mae = models.CharField(max_length=200)
  sexo = models.CharField(max_length=1)
  Doencas_id = models.ForeignKey(Doencas, on_delete=models.CASCADE, default=None, blank=True, null=True)
  uf_id = models.ForeignKey(Uf, on_delete=models.CASCADE)
  Municipio_id = models.ForeignKey(Municipio, on_delete=models.CASCADE, default=None, blank=True, null=True)
  Login_id = models.ForeignKey(Login, on_delete=models.CASCADE)
  Medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE, default=None, blank=True, null=True)

  def __str__(self):
    return self.nome
  