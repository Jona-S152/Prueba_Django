from django.db import models

# Create your models here.
class Persona(models.Model):
    idPersona = models.IntegerField(primary_key=True, auto_created=True, blank=True)
    Nombres = models.CharField(max_length=60)
    Apellidos = models.CharField(max_length=60)
    Identificacion = models.CharField(max_length=10)
    FechaNacimiento = models.DateField()

class Usuarios(models.Model):
    idUsuario = models.IntegerField(primary_key=True, auto_created=True)
    UserName = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Mail = models.CharField(max_length=120)
    SessionActive = models.CharField(max_length=1)
    Persona_idPersona2 = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Sessions(models.Model):
    FechaIngreso = models.DateField()
    FechaCierre = models.DateField()
    Usuarios_idUsuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

class Rol(models.Model):
    idRol = models.IntegerField(primary_key= True, auto_created=True)
    RolName = models.CharField(max_length=50)

class Rol_Usuarios(models.Model):
    Rol_idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    Usuarios_idUsuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

class Rol_Opciones(models.Model):
    NombreOpcion = models.CharField(max_length=50)
    idOpcion = models.IntegerField(primary_key=True, auto_created=True)

class Rol_RolOpciones(models.Model):
    Rol_idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    RolOpciones_idOpcion = models.ForeignKey(Rol_Opciones, on_delete=models.CASCADE)

