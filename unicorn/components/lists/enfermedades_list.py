from django_unicorn.components import UnicornView
from user.models import Enfermedad
from ai.inferenceEngine.learning import is_fact, delete_fact

class EnfermedadesListView(UnicornView):
    enfermedades = Enfermedad.objects.none()

    def mount(self):
        self.load_table()

    def hydrate(self):
        self.load_table()

    def load_table(self):
        self.enfermedades = Enfermedad.objects.all()

    def delete_enfermedad(self, id):
        enfermedad = Enfermedad.objects.get(id=id)
        self.delete_enfermedad_prolog(enfermedad)
        enfermedad.delete()
        self.call("alerta_eliminacion_satisfactoria")

    def delete_enfermedad_prolog(self, enfermedad):
        sintomas = enfermedad.sintomas.values_list('nombre', flat=True)
        signos = enfermedad.signos.values_list('nombre', flat=True)
        pruebas_lab = enfermedad.pruebasLaboratorio.values_list('nombre', flat=True)
        pruebas_post = enfermedad.pruebasPostmorten.values_list('nombre', flat=True)

        if len(list(sintomas)) > 0:
            for sintoma in list(sintomas):
                fact = f"symptom({sintoma},{enfermedad.nombre})"
                if is_fact(fact):
                    delete_fact(fact)

        if len(list(signos)) > 0:
            for signo in list(signos):
                fact = f"sign({signo},{enfermedad.nombre})"
                if is_fact(fact):
                    delete_fact(fact)

        if len(list(pruebas_lab)) > 0:
            for prueba_lab in list(pruebas_lab):
                fact = f"lab_test({prueba_lab},{enfermedad.nombre})"
                if is_fact(fact):
                    delete_fact(fact)

        if len(list(pruebas_post)) > 0:
            for prueba_post in list(pruebas_post):
                fact = f"postmortem_test({prueba_post},{enfermedad.nombre})"
                if is_fact(fact):
                    delete_fact(fact)
