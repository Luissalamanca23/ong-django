from django.db import models

# Create your models here.

class gato(models.Model):
    id_gato = models.AutoField(primary_key=True);
    nombre = models.CharField(max_length=100);
    edad = models.IntegerField();
    raza = models.CharField(max_length=100);
    esterilizado = models.BooleanField();


    def __str__(self):
 