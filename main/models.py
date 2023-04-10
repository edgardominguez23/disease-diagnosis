from django.db import models

# Create your models here.

class Signo(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'signos'

class Sintoma(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'sintomas'

class PruebaLaboratorio(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'pruebas_laboratorio'

class PruebaPostmorten(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'pruebas_postmorten'

class Enfermedad(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False)
    sintomas = models.ManyToManyField(Sintoma, db_table='enfermedades_sintomas', related_name='enfermedades')
    signos = models.ManyToManyField(Signo, db_table='enfermedades_signos', related_name='enfermedades')
    pruebasLaboratorio = models.ManyToManyField(PruebaLaboratorio, db_table='enfermedades_pruebas_laboratorio', related_name='enfermedades')
    pruebasPostmorten = models.ManyToManyField(PruebaPostmorten, db_table='enfermedades_pruebas_postmorten', related_name='enfermedades')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'enfermedades'
