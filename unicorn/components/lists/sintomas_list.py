from django_unicorn.components import UnicornView
from django.core.paginator import Paginator
from main.models import Sintoma
from main.forms import SintomaForm

class SintomasListView(UnicornView):
    sintoma = None
    isOpenModal = "hidden"

    page_index = 1
    paginator = None
    page = None
    page_range = None

    form_class = SintomaForm
    nombre = ""

    class Meta:
        exclude = ()
        javascript_exclude = (
            "paginator",
            "page",
            "page_range",
        )

    def mount(self):
        self.load_table()

    def hydrate(self):
        self.load_table()

    def load_table(self):
        qs = Sintoma.objects.order_by('id')
        self.paginator = Paginator(qs, 10)
        self.page = self.paginator.page(self.page_index)

    def open_modal(self, id=None):
        self.form_class = SintomaForm
        self.isOpenModal = ""

        if id:
            self.sintoma = Sintoma.objects.get(id=id)
            self.nombre = self.sintoma.nombre

    def close_modal(self):
        self.restablecer_valores()

    def save_sintoma(self):
        if self.is_valid() and self.validar_nombre_unico():
            if self.sintoma:
                self.sintoma.nombre = self.nombre
                self.sintoma.save()
                self.call("alerta_actualizacion_satisfactoria")
            else:
                sintoma = Sintoma(nombre=self.nombre)
                sintoma.save()
                self.call("alerta_creacion_satisfactoria")

            self.restablecer_valores()

    def delete_sintoma(self, id):
        sintoma = Sintoma.objects.get(id=id)
        sintoma.delete()
        self.call("alerta_eliminacion_satisfactoria")

    def restablecer_valores(self):
        self.nombre = ""
        self.sintoma = None
        self.isOpenModal = "hidden"

    def validar_nombre_unico(self):
        if self.sintoma:
            if not self.sintoma.nombre == self.nombre:
                if Sintoma.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        else:
            if Sintoma.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        
        return True
    
    def cambiar_pagina(self, number):
        self.page_index = number
        self.load_table()

    def siguiente_pagina(self):
        if self.page.has_next():
            self.page_index += 1
            self.load_table()

    def regresar_pagina(self):
        if self.page.has_previous():
            self.page_index -= 1
            self.load_table()