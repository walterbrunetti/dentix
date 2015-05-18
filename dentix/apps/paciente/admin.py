from django.contrib import admin
from models import Paciente


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellido', 'telefono', 'celular', 'obra_social')
    search_fields = ['dni', 'nombre', 'apellido']


admin.site.register(Paciente, PacienteAdmin)
