from django.contrib import admin
from models import ObraSocial


class ObraSocialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'direccion')
    search_fields = ['nombre', ]


admin.site.register(ObraSocial, ObraSocialAdmin)
