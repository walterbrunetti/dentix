from django.contrib import admin
from models import Presentacion, Ficha
from dentix.apps.tratamiento.models import DetallePrestacion

class FichaInline(admin.TabularInline):
    readonly_fields = ['get_details_link', ]
    model = Ficha
    raw_id_fields = ('paciente', )


class PresentacionAdmin(admin.ModelAdmin):
    inlines = [
        FichaInline,
    ]
    list_display = ('fecha', 'entidad')
    search_fields = ['fecha', ]
    list_filter = ('entidad', )


class DetallePrestacionInline(admin.TabularInline):
    model = DetallePrestacion
    raw_id_fields = ('tratamiento', )


class FichaAdmin(admin.ModelAdmin):
    inlines = [
        DetallePrestacionInline,
    ]
    list_display = ('presentacion', 'paciente', 'importe_estimado', 'importe_cobrado', 'estado')
    search_fields = ['paciente__nombre', 'paciente__apellido', 'presentacion__fecha']
    list_filter = ('estado', 'presentacion__entidad')
    raw_id_fields = ('paciente', 'presentacion')
    readonly_fields = ('foto_f1_tag',)


admin.site.register(Presentacion, PresentacionAdmin)
admin.site.register(Ficha, FichaAdmin)

