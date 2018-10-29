from django.db import models
# Create your models here.
class Investigacion(models.Model):
    titulo=models.CharField(max_length=250,null=True)
    autor=models.CharField(max_length=250,null=True)
    content= models.FileField(null=True);
    CATEGORIA = (
        ('CiCom', 'Ciencias Computacionales'),
        ('CiTi', 'Ciencias de la Tierra'),
        ('CiNa', 'Ciencias Naturales'),
        ('CiSo', 'Ciencias Sociales'),
        ('CiMe', 'Ciencias Medicas'),
    )
    categoria= models.CharField(max_length=50,choices=CATEGORIA,
                                      default='CiCom')
    def __str__(self):
             return self.autor
