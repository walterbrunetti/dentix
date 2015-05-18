from django.contrib import admin
from models import Prestacion


class PrestacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')
    search_fields = ['nombre', 'codigo',]


admin.site.register(Prestacion, PrestacionAdmin)

