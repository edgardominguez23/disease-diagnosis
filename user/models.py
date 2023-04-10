from django.db import models
from enum import Enum
from django.contrib.auth.models import User
from main.models import Enfermedad
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Direccion(models.Model):
    municipio = models.CharField(max_length=50, null=False) 
    colonia = models.CharField(max_length=30, null=False)
    codigoPostal = models.CharField(max_length=5, null=False)
    calle = models.CharField(max_length=50, null=False)
    numero = models.PositiveIntegerField(null=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'direcciones'


class Consultorio(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False)
    hora_abierto = models.TimeField(null=False) 
    hora_cerrado = models.TimeField(null=False)
    direccion = GenericRelation(Direccion)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'consultorios'

class Paciente(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    apellidos = models.CharField(max_length=255, null=False)
    telefono = models.CharField(max_length=10, null=False)
    direccion = GenericRelation(Direccion)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pacientes'

class Cita(models.Model):
    class EstadoCita(Enum):
        PROGRAMADA = 'Programada'
        CONFIRMADA = 'Confirmada'
        EN_ESPERA = 'En espera'
        EN_CURSO = 'En curso'
        CANCELADA_PACIENTE = 'Cancelada por el paciente'
        CANCELADA_MEDICO = 'Cancelada por el médico'
        COMPLETADA = 'Completada'
        NO_PRESENTADO = 'No presentado'

    fecha = models.DateField(null=False)
    hora = models.TimeField(null=False)
    estado = models.CharField(max_length=20, choices=[(estado.name, estado.value) for estado in EstadoCita])
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE, related_name='citas')
    secretaria = models.ForeignKey(User, on_delete=models.CASCADE, related_name='citasCreadas')
    medico =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='citasAsignadas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'citas'

class Consulta(models.Model):
    motivo = models.TextField(null=False)
    diagnostico = models.TextField(null=False)
    tratamiento = models.TextField(null=False)
    cita = models.OneToOneField(Cita, on_delete=models.CASCADE, related_name='consulta')
    medico =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultas')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    enfermedades = models.ManyToManyField(Enfermedad, db_table='consultas_enfermedades')

    class Meta:
        db_table = 'consultas'

class HistorialConsultas(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='historial')
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'historial_consultas'

