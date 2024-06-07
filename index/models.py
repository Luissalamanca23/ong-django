from django.db import models

# Create your models here.

class Gato(models.Model):
    id_gato = models.AutoField(primary_key=True);
    nombre = models.CharField(max_length=100);
    edad = models.IntegerField();
    raza = models.CharField(max_length=100);
    esterilizado = models.BooleanField();
    fecha_nacimiento = models.DateField();


    def __str__(self):
        return str(self.id_gato) + " " + str(self.nombre);
 