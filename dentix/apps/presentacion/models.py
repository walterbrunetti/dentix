from django.db import models
from dentix.apps.paciente.models import Paciente


ENTIDADES = (
    (1, 'Asor'),
    (2, 'Ale vanucci'),
)


ESTADOS = (
    (1, 'Pendiente'),
    (2, 'Pagado'),
    (2, 'No Pagado'),
)


class Presentacion(models.Model):
    fecha = models.DateField()
    entidad = models.SmallIntegerField(choices=ENTIDADES)

    def __unicode__(self):
        return u'%s - %s' % (self.fecha, ENTIDADES[self.entidad - 1][1])


class Ficha(models.Model):
    paciente = models.ForeignKey(Paciente)
    foto_f1 = models.FileField(upload_to='uploads_imgs', null=True, blank=True)
    copago = models.DecimalField(max_digits=16, decimal_places=2)
    estampilla = models.DecimalField(max_digits=16, decimal_places=2)
    presentacion = models.ForeignKey(Presentacion)
    importe_estimado = models.DecimalField(max_digits=16, decimal_places=2)
    importe_cobrado = models.DecimalField(max_digits=16, decimal_places=2)
    estado = models.SmallIntegerField(choices=ESTADOS)

    def __unicode__(self):
        return u'%s %s %s' % (self.paciente, self.presentacion.fecha, ENTIDADES[self.presentacion.entidad - 1][1])


