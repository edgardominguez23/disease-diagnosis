from django import forms
from django.utils.translation import gettext_lazy as _

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
