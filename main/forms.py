from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

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