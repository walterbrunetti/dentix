from django.contrib import admin

from models import Diente, Tratamiento, DetallePrestacion, Visita


class DetallePrestacionInline(admin.TabularInline):
    model = DetallePrestacion


class VisitaInline(admin.TabularInline):
    model = Visita


class TratamientoAdmin(admin.ModelAdmin):
    inlines = [
        DetallePrestacionInline,
        VisitaInline,
    ]

admin.site.register(Tratamiento, TratamientoAdmin)
admin.site.register(Diente)
#admin.site.register(DetallePrestacion)
#admin.site.register(Visita)

