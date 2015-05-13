from django.db import models

class Prestacion(models.Model):
    nombre = models.CharField(max_length=128)
    codigo = models.CharField(max_length=128)

    def __unicode__(self):
        return self.nombre

