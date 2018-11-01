from django.db import models

# Create your models here.


class Departamento(models.Model):
    depa= models.CharField(max_length=200)

    def __str__(self):
        return self.depa

class Software(models.Model):
    nombreSoftware= models.CharField(max_length=200)
    funcion=  models.CharField(max_length=200)
    departamento= models.ForeignKey(Departamento, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombreSoftware
