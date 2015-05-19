from django.db import models
from dentix.apps.paciente.models import Paciente


ENTIDADES = (
    (1, 'Asor'),
    (2, 'Ale vanucci'),
)


ESTADOS = (
    (1, 'Pendiente'),
    (2, 'Pagado'),
    (3, 'No Pagado'),
)


class Presentacion(models.Model):
    fecha = models.DateField()
    entidad = models.SmallIntegerField(choices=ENTIDADES)

    def __unicode__(self):
        return u'%s - %s' % (self.fecha, ENTIDADES[self.entidad - 1][1])


class Ficha(models.Model):
    paciente = models.ForeignKey(Paciente)
    foto_f1 = models.FileField(upload_to='uploads_imgs', null=True, blank=True)
    copago = models.DecimalField(max_digits=5, decimal_places=2)
    estampilla = models.DecimalField(max_digits=5, decimal_places=2)
    presentacion = models.ForeignKey(Presentacion)
    importe_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    importe_cobrado = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.SmallIntegerField(choices=ESTADOS)

    def get_details_link(self):
        if self.id:
            return u'<a href="/admin/presentacion/ficha/%s" target="_blank">Detalle</a>' % self.id
        return u''

    get_details_link.allow_tags = True

    def foto_f1_tag(self):
        if self.foto_f1:
            return u'<a href="/media/%s" target="_blank"><img src="/media/%s" style="width:500px;" /></a>' % (self.foto_f1.name, self.foto_f1.name)
        return u''
    foto_f1_tag.short_description = 'Foto f1 preview'
    foto_f1_tag.allow_tags = True

    def __unicode__(self):
        return u'%s %s %s' % (self.paciente, self.presentacion.fecha, ENTIDADES[self.presentacion.entidad - 1][1])


