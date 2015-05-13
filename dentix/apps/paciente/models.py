from django.db import models
from dentix.apps.obrasocial.models import ObraSocial


SEXO = (
    (1, 'masculino'),
    (2, 'femenino'),
)


class Paciente(models.Model):
    dni = models.IntegerField()
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    domicilio = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=200)
    celular = models.CharField(max_length=200, null=True, blank=True)
    sexo = models.SmallIntegerField(choices=SEXO)
    email = models.CharField(max_length=200, null=True, blank=True)
    
    obra_social = models.ForeignKey(ObraSocial)


    def __unicode__(self):
        return u'%s, %s' % (self.apellido, self.nombre)

