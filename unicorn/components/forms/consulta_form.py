from django_unicorn.components import UnicornView
from ai.inferenceEngine.learning import show_symptoms, show_signs
from ai.inferenceEngine.engine import diagnose
from multiprocessing import Process, Queue

class ConsultaFormView(UnicornView):
    symptoms = show_symptoms()
    signs = show_signs()
    test = []

    def obtener_diagnostico(self):
        #padecimientos = self.signos + self.sintomas
        queue = Queue()
        p = Process(target=diagnose, args=(['cansancio'], queue))
        p.start()
        
        # Esperar a que se completen los resultados
        p.join()
        results = queue.get()

        print(results)

    def get_consulta(self, padecimientos):
        #padecimientos = self.signos + self.sintomas
        queue = Queue()
        p = Process(target=diagnose, args=(padecimientos.split(","), queue))
        p.start()
        
        # Esperar a que se completen los resultados
        p.join()
        self.test = queue.get()
        print(self.test)
