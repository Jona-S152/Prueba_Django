from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status, viewsets
from .models import Persona, Usuarios, Rol
from .serializers import PersonaSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def crear(request):
	serializer = PersonaSerializer(data=request.data)
 
	if Persona.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')
 
	if serializer.is_valid():
		persona = serializer.save()
		data = PersonaSerializer(persona).data
		return Response(data, status=status.HTTP_201_CREATED)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def listar(request):
    personas = Persona.objects.all()

    if personas:
        personaSerializer = PersonaSerializer(personas, many=True)

        return Response(personaSerializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def actualizar(request, id):
	
	person = Persona.objects.get(pk=id)
	serializer = PersonaSerializer(instance=person, data=request.data)
 
	if serializer.is_valid():
		persona = serializer.save()
		data = PersonaSerializer(persona).data
		return Response(data, status=status.HTTP_200_OK)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
@api_view(['DELETE'])
def eliminar(request, id):
    persona = get_object_or_404(Persona, pk=id)
    persona.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def buscar(request, id):
	persona = Persona.objects.filter(pk=id)
	#person = get_object_or_404(Persona, pk=id)
	if persona:
		serializer = PersonaSerializer(instance=persona, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	return Response(status=status.HTTP_404_NOT_FOUND)