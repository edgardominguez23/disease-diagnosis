from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

class EnfermedadForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo nombre es requerido.'),
                'max_length': _('El campo nombre debe tener como máximo 50 caracteres.'),
            })
class SintomaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo nombre es requerido.'),
                'max_length': _('El campo nombre debe tener como máximo 50 caracteres.'),
            })
    
class SignoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo nombre es requerido.'),
                'max_length': _('El campo nombre debe tener como máximo 50 caracteres.'),
            })
    
class PruebaLaboratorioForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo nombre es requerido.'),
                'max_length': _('El campo nombre debe tener como máximo 50 caracteres.'),
            })
    
class PruebaPostmortenForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo nombre es requerido.'),
                'max_length': _('El campo nombre debe tener como máximo 50 caracteres.'),
            })
    
class ConsultorioForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo nombre es requerido.'),
                'max_length': _('El campo nombre debe tener como máximo 50 caracteres.'),
            })
    hora_abierto = forms.TimeField(required=True, error_messages={
                'required': _('Este campo hora inicial es requerido.'),
                'invalid': _('Ingrese un tiempo válido en el formato HH:MM:SS'),
            })
    hora_cerrado = forms.TimeField(required=True, error_messages={
                'required': _('Este campo hora final es requerido.'),
                'invalid': _('Ingrese un tiempo válido en el formato HH:MM:SS'),
            })
    municipio = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo municipio es requerido.'),
                'max_length': _('El campo municipio debe tener como máximo 50 caracteres.'),
            })
    colonia = forms.CharField(max_length=30, required=True, error_messages={
                'required': _('Este campo colonia es requerido.'),
                'max_length': _('El campo colonia debe tener como máximo 50 caracteres.'),
            })
    codigoPostal = forms.IntegerField(max_value=50000, min_value=40000, required=True, error_messages={
                'required': _('Este campo codigo postal es requerido.'),
            })
    calle = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo calle es requerido.'),
                'max_length': _('El campo calle debe tener como máximo 50 caracteres.'),
            })
    numero = forms.IntegerField(max_value=50000, min_value=1, required=True, error_messages={
                'required': _('Este campo numero es requerido.'),
            })
    
class PacienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo nombre es requerido.'),
                'max_length': _('El campo nombre debe tener como máximo 50 caracteres.'),
            })
    apellidos = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo apellidos es requerido.'),
                'max_length': _('El campo nombre debe tener como máximo 50 caracteres.'),
            })
    telefono = forms.IntegerField(max_value=9999999999, min_value=10000000, required=True, error_messages={
                'required': _('Este campo telefono es requerido.'),
            })
    municipio = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo municipio es requerido.'),
                'max_length': _('El campo municipio debe tener como máximo 50 caracteres.'),
            })
    colonia = forms.CharField(max_length=30, required=True, error_messages={
                'required': _('Este campo colonia es requerido.'),
                'max_length': _('El campo colonia debe tener como máximo 50 caracteres.'),
            })
    codigoPostal = forms.IntegerField(max_value=50000, min_value=40000, required=True, error_messages={
                'required': _('Este campo codigo postal es requerido.'),
            })
    calle = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo calle es requerido.'),
                'max_length': _('El campo calle debe tener como máximo 50 caracteres.'),
            })
    numero = forms.IntegerField(max_value=50000, min_value=1, required=True, error_messages={
                'required': _('Este campo numero es requerido.'),
            })
    
class UsuarioForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo nombre es requerido.'),
                'max_length': _('El campo nombre debe tener como máximo 50 caracteres.'),
            })
    first_name = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo nombre es requerido.'),
                'max_length': _('El campo nombre debe tener como máximo 50 caracteres.'),
            })
    last_name = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo apellidos es requerido.'),
                'max_length': _('El campo apellidos debe tener como máximo 50 caracteres.'),
            })
    email = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo correo es requerido.'),
                'max_length': _('El campo correo debe tener como máximo 50 caracteres.'),
            })
    rol = forms.CharField(max_length=50, required=True, error_messages={
                'required': _('Este campo rol es requerido.'),
            })
    
class CitaForm(forms.Form):
    fecha = forms.DateField(required=True, error_messages={ 'required': _('La fecha es requerida.') })
    hora = forms.TimeField(required=True, error_messages={ 'required': _('La hora es requerida.') })
    estado = forms.CharField(required=True, error_messages={ 'required': _('El estado es requerido.') })
    paciente = forms.CharField(required=True, error_messages={ 'required': _('El paciente es requerido.') })
    consultorio = forms.CharField(required=True, error_messages={ 'required': _('El consultorio es requerido.') })
    medico = forms.CharField(required=True, error_messages={ 'required': _('El medico es requerido.') })