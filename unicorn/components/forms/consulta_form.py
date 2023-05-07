from django_unicorn.components import UnicornView
from ai.inferenceEngine.learning import show_symptoms, show_signs
from ai.inferenceEngine.engine import diagnose

class ConsultaFormView(UnicornView):
    symptoms = show_symptoms()
    signs = show_signs()

    signos = []
    sintomas = []

    def obtener_diagnostico(self):
        padecimientos = self.signos + self.sintomas
        diagnostico = diagnose(padecimientos)
        print(diagnostico)
