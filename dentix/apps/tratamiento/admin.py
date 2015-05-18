from django.contrib import admin

from models import Diente, Tratamiento, DetallePrestacion, Visita


class DetallePrestacionInline(admin.TabularInline):
    model = DetallePrestacion
    raw_id_fields = ('ficha', )


class VisitaInline(admin.TabularInline):
    model = Visita


class TratamientoAdmin(admin.ModelAdmin):
    inlines = [
        DetallePrestacionInline,
        VisitaInline,
    ]
    list_display = ('fecha', 'paciente', 'estado')
    search_fields = ['fecha', 'paciente__nombre', 'paciente__apellido']
    list_filter = ('estado', )
    raw_id_fields = ('paciente', )
    readonly_fields = ('foto_f3_tag',)

admin.site.register(Tratamiento, TratamientoAdmin)
admin.site.register(Diente)
#admin.site.register(DetallePrestacion)
#admin.site.register(Visita)

