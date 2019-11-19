from django.db import models

# Create your models here.
class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    stock=models.IntegerField()
    foto=models.ImageField(upload_to='fotos/')

    def __str__(self):
        return str(self.id)+", "+self.nombre+", "+str(self.precio)+", "+str(self.stock)+", "+str(self.foto)


class Registro(models.Model):
    correo=models.CharField(max_length=100, primary_key=True)
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    contrasenia=models.CharField(max_length=16)

    def __str__(self):
        return self.correo+", "+self.nombre+", "+self.apellido+", "+self.contrasenia

class Contactenos(models.Model):
    id=models.AutoField(primary_key=True)
    correo=models.CharField(max_length=100)
    mensaje=models.CharField(max_length=250)
