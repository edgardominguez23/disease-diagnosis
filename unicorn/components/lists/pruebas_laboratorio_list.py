from django_unicorn.components import UnicornView
from django.core.paginator import Paginator
from main.models import PruebaLaboratorio
from main.forms import PruebaLaboratorioForm

class PruebasLaboratorioListView(UnicornView):
    prueba = None
    isOpenModal = "hidden"

    page_index = 1
    paginator = None
    page = None
    page_range = None

    form_class = PruebaLaboratorioForm
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
        qs = PruebaLaboratorio.objects.order_by('id')
        self.paginator = Paginator(qs, 10)
        self.page = self.paginator.page(self.page_index)

    def open_modal(self, id=None):
        self.form_class = PruebaLaboratorioForm
        self.isOpenModal = ""

        if id:
            self.prueba = PruebaLaboratorio.objects.get(id=id)
            self.nombre = self.prueba.nombre

    def close_modal(self):
        self.restablecer_valores()

    def save_prueba(self):
        if self.is_valid() and self.validar_nombre_unico():
            if self.prueba:
                self.prueba.nombre = self.nombre
                self.prueba.save()
                self.call("alerta_actualizacion_satisfactoria")
            else:
                prueba = PruebaLaboratorio(nombre=self.nombre)
                prueba.save()
                self.call("alerta_creacion_satisfactoria")

            self.restablecer_valores()

    def delete_prueba(self, id):
        prueba = PruebaLaboratorio.objects.get(id=id)
        prueba.delete()
        self.call("alerta_eliminacion_satisfactoria")

    def restablecer_valores(self):
        self.nombre = ""
        self.prueba = None
        self.isOpenModal = "hidden"

    def validar_nombre_unico(self):
        if self.prueba:
            if not self.prueba.nombre == self.nombre:
                if PruebaLaboratorio.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        else:
            if PruebaLaboratorio.objects.filter(nombre=self.nombre).exists():
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