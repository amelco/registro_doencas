from django.contrib import admin
from .models import Gestor, Login, Tipo_usuario, Pacientes, Doencas, Uf, Medico, Municipio


admin.site.register(Gestor)
admin.site.register(Login)
admin.site.register(Tipo_usuario)
admin.site.register(Pacientes)
admin.site.register(Doencas)
admin.site.register(Uf)
admin.site.register(Municipio)
admin.site.register(Medico)