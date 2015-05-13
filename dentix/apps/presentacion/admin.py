from django.contrib import admin
from models import Presentacion, Ficha
from dentix.apps.tratamiento.models import DetallePrestacion

class FichaInline(admin.TabularInline):
    model = Ficha


class PresentacionAdmin(admin.ModelAdmin):
    inlines = [
        FichaInline,
    ]


class DetallePrestacionInline(admin.TabularInline):
    model = DetallePrestacion


class FichaAdmin(admin.ModelAdmin):
    inlines = [
        DetallePrestacionInline,
    ]
    pass

admin.site.register(Presentacion, PresentacionAdmin)
admin.site.register(Ficha, FichaAdmin)

