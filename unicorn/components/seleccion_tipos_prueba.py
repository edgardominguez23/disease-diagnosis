from django_unicorn.components import UnicornView


class SeleccionTiposPruebaView(UnicornView):
    tipo = None
    estaSeleccionadoLaboratorio = None

    def mount(self):
        self.tipo = '0'

    def estaSeleccionadoLaboratorio(self):
        return "" if self.tipo == '0' else "hidden"
    
    def estaSeleccionadoPostmortem(self):
        return "" if self.tipo == '1' else "hidden"
