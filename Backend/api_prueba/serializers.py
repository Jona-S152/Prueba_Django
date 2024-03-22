from rest_framework import serializers
from .models import Persona, Usuarios, Sessions, Rol, Rol_Usuarios, Rol_Opciones, Rol_RolOpciones

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = [
            'idPersona',
            'Nombres',
            'Apellidos',
            'Identificacion',
            'FechaNacimiento'
        ]

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = [
            'idUsuario',
            'UserName',
            'Password',
            'Mail',
            'SessionActive',
            'Persona_idPersona2'
        ]

class USessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessions
        fields = [
            'FechaIngreso',
            'FechaCierre',
            'Usuarios_idUsuario'
        ]

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = [
            'idRol',
            'RolName'
        ]

class Rol_UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol_Usuarios
        fields = [
            'Rol_idRol',
            'Usuarios_idUsuario'
        ]

class Rol_OpcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol_Opciones
        fields = [
            'NombreOpcion',
            'idOpcion'
        ]

class Rol_RolOpcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol_RolOpciones
        fields = [
            'Rol_idRol',
            'RolOpciones_idOpcion'
        ]