from django_unicorn.components import UnicornView
from user.models import Enfermedad
from main.models import Signo, Sintoma, PruebaLaboratorio, PruebaPostmorten
from main.forms import EnfermedadForm
from ai.inferenceEngine.learning import is_fact, add_fact, delete_fact

class EnfermedadFormView(UnicornView):
    enfermedad = None

    signos = None
    sintomas = None
    pruebas_post = None
    pruebas_lab = None

    form_class = EnfermedadForm
    nombre = ""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.enfermedad = None if kwargs.get("enfermedad") == 'enfermedad' else kwargs.get("enfermedad")

        self.signos = Signo.objects.all()
        self.sintomas = Sintoma.objects.all()
        self.pruebas_post = PruebaPostmorten.objects.all()
        self.pruebas_lab = PruebaLaboratorio.objects.all()

    def mount(self):
        if self.enfermedad:
            self.nombre = self.enfermedad.nombre

    def save_enfermedad(self, sintomas, signos, pruebas_lab, pruebas_post):
        self.sintomas = sintomas.split(",")
        self.signos = signos.split(",")
        self.pruebas_lab = pruebas_lab.split(",")
        self.pruebas_post = pruebas_post.split(",")

        if self.is_valid() and self.validar_nombre_unico():
            if self.enfermedad:
                self.enfermedad.nombre = self.nombre.lower()
                self.enfermedad.save()
                self.save_enfermedad_prolog(self.enfermedad)

                self.call("alerta_actualizacion_satisfactoria")
            else:
                enfermedad = Enfermedad(
                                nombre=self.nombre.lower(),
                            )
                enfermedad.save()
                self.save_enfermedad_prolog(enfermedad)

                self.call("alerta_creacion_satisfactoria")

    def validar_nombre_unico(self):
        if self.enfermedad:
            if not self.enfermedad.nombre == self.nombre:
                if Enfermedad.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        else:
            if Enfermedad.objects.filter(nombre=self.nombre).exists():
                    self.call("alerta_nombre_existente")
                    return False
        
        return True
    
    def save_enfermedad_prolog(self, enfermedad):
        if not self.sintomas[0] == '':
            enfermedad.sintomas.set(self.sintomas)
            for sintoma in self.sintomas:
                fact = f"symptom({Sintoma.objects.get(id=sintoma).nombre},{enfermedad.nombre})"
                if not is_fact(fact):
                    add_fact(fact)

        if not self.signos[0] == '':
            enfermedad.signos.set(self.sintomas)
            for signo in self.signos:
                fact = f"sign({Signo.objects.get(id=signo).nombre},{enfermedad.nombre})"
                if not is_fact(fact):
                    add_fact(fact)

        if not self.pruebas_lab[0] == '':
            enfermedad.pruebasLaboratorio.set(self.pruebas_lab)
            for prueba_lab in self.pruebas_lab:
                fact = f"lab_test({PruebaLaboratorio.objects.get(id=prueba_lab).nombre},{enfermedad.nombre})"
                if not is_fact(fact):
                    add_fact(fact)

        if not self.pruebas_post[0] == '':
            enfermedad.pruebasPostmorten.set(self.pruebas_post)
            for prueba_post in self.pruebas_post:
                fact = f"postmortem_test({PruebaPostmorten.objects.get(id=prueba_post).nombre},{enfermedad.nombre})"
                if not is_fact(fact):
                    add_fact(fact)


