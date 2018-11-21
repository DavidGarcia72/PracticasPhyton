from django.db import models
from django.conf import settings
# Create your models here.
class Ki(models.Model):
    personaje = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    nivelDePoder= models.IntegerField()
    tipoRaza = (
    ('Saiyajin','SAIYAJIN'),
    ('Nameku', 'NAMEKU'),
    ('Humano','HUMANO'),
    ('Majin','MAJIN'),
)
    raza=models.CharField(max_length=8, choices=tipoRaza, default='Saiyajin')
    habilidad = models.CharField(max_length=250)

    def __str__(self):
        return self.habilidad
