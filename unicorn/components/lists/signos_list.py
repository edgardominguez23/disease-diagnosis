from django_unicorn.components import UnicornView
from django.core.paginator import Paginator
from main.models import Signo
from main.forms import SignoForm

class SignosListView(UnicornView):
    signo = None
    isOpenModal = "hidden"

    page_index = 1
    paginator = None
    page = None
    page_range = None

    form_class = SignoForm
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
        qs = Signo.objects.order_by('id')
        self.paginator = Paginator(qs, 10)
        self.page = self.paginator.page(self.page_index)

    def open_modal(self, id=None):
        self.form_class = SignoForm
        self.isOpenModal = ""

        if id:
            self.signo = Signo.objects.get(id=id)
            self.nombre = self.signo.nombre

    def close_modal(self):
        self.restablecer_valores()

    def save_signo(self):
        if self.is_valid() and self.validar_nombre_unico():
            if self.signo:
                self.signo.nombre = self.nombre
                self.signo.save()
                self.call("alerta_actualizacion_satisfactoria")
            else:
                signo = Signo(nombre=self.nombre)
                signo.save()
                self.call("alerta_creacion_satisfactoria")

            self.restablecer_valores()

    def delete_signo(self, id):
        signo = Signo.objects.get(id=id)
        signo.delete()
        self.call("alerta_eliminacion_satisfactoria")

    def restablecer_valores(self):
        self.nombre = ""
        self.signo = None
        self.isOpenModal = "hidden"

    def validar_nombre_unico(self):
        if self.signo:
            if not self.signo.nombre == self.nombre:
                if Signo.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        else:
            if Signo.objects.filter(nombre=self.nombre).exists():
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
