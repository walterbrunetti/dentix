from django.db import models
from dentix.apps.paciente.models import Paciente
from dentix.apps.prestacion.models import Prestacion
from dentix.apps.presentacion.models import Presentacion, Ficha



ESTADOS = (
    (1, 'Finalizado'),
    (2, 'En Proceso'),
    (3, 'Suspendido'),
)


class Diente(models.Model):
    nombre = models.CharField(max_length=128)
    nro_diente = models.CharField(max_length=128)

    def __unicode__(self):
        return u'%s - %s' % (self.nro_diente, self.nombre)


class Cara(models.Model):
    nombre = models.CharField(max_length=128)

    def __unicode__(self):
        return self.nombre


class Tratamiento(models.Model):
    fecha = models.DateField()
    paciente = models.ForeignKey(Paciente)
    estado = models.SmallIntegerField(choices=ESTADOS)
    foto_f3 = models.FileField(upload_to='uploads_imgs', null=True, blank=True)
    observaciones = models.TextField(max_length=1024, null=True, blank=True)

    def foto_f3_tag(self):
        if self.foto_f3:
            return u'<a href="/media/%s" target="_blank"><img src="/media/%s" style="width:500px;" /></a>' % (self.foto_f3.name, self.foto_f3.name)
        return u''
    foto_f3_tag.short_description = 'Foto f3 preview'
    foto_f3_tag.allow_tags = True

    def __unicode__(self):
        return u'%s, %s' % (self.paciente.apellido, self.paciente.nombre)


class DetallePrestacion(models.Model):
    prestacion = models.ForeignKey(Prestacion)
    diente = models.ForeignKey(Diente, null=True, blank=True)
    cara = models.ForeignKey(Cara, null=True, blank=True)
    tratamiento = models.ForeignKey(Tratamiento)  # Un tratamiento tiene muchos detalles de prestacion
    ficha = models.ForeignKey(Ficha, null=True, blank=True)

    def __unicode__(self):
        return u'%s %s %s' % (self.prestacion.nombre, self.diente, self.tratamiento.paciente)
    

class Visita(models.Model):
    fecha = models.DateField()
    observaciones = models.TextField(max_length=1024, null=True, blank=True)
    tratamiento = models.ForeignKey(Tratamiento)

