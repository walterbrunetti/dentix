from django.db import models

class ObraSocial(models.Model):
    nombre = models.CharField(max_length=128)
    telefono = models.CharField(max_length=128, null=True, blank=True)
    direccion = models.CharField(max_length=128, null=True, blank=True)
    observaciones = models.TextField(max_length=1024, null=True, blank=True)

    def __unicode__(self):
        return self.nombre


