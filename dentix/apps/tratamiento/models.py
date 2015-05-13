from django.db import models
from dentix.apps.paciente.models import Paciente
from dentix.apps.prestacion.models import Prestacion
from dentix.apps.presentacion.models import Presentacion, Ficha



ESTADOS = (
    (1, 'Finalizado'),
    (2, 'En Proceso'),
    (3, 'Suspendido'),
)


CARA_CHOICES = (
    (1, 'Distal'),
    (2, 'Mesial'),
    (3, 'Oclusal'),
    (4, 'Incisal'),
)


class Diente(models.Model):
    nombre = models.CharField(max_length=128)
    nro_diente = models.CharField(max_length=128)

    def __unicode__(self):
        return u'%s - %s' % (self.nro_diente, self.nombre)


class Tratamiento(models.Model):
    fecha = models.DateField()
    paciente = models.ForeignKey(Paciente)
    estado = models.SmallIntegerField(choices=ESTADOS)
    foto_f3 = models.FileField(upload_to='uploads_imgs', null=True, blank=True)
    observaciones = models.TextField(max_length=1024, null=True, blank=True)


    def __unicode__(self):
        return self.paciente.nombre


class DetallePrestacion(models.Model):
    prestacion = models.ForeignKey(Prestacion)
    diente = models.ForeignKey(Diente, null=True, blank=True)
    cara = models.SmallIntegerField(choices=CARA_CHOICES, null=True, blank=True)
    tratamiento = models.ForeignKey(Tratamiento)  # Un tratamiento tiene muchos detalles de prestacion
    ficha = models.ForeignKey(Ficha, null=True, blank=True)

    def __unicode__(self):
        return u'%s %s %s' % (self.prestacion.nombre, self.diente, self.tratamiento.paciente)
    

class Visita(models.Model):
    fecha = models.DateField()
    observaciones = models.TextField(max_length=1024, null=True, blank=True)
    tratamiento = models.ForeignKey(Tratamiento)

