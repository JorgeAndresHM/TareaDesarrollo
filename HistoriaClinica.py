

class HistoriaClinica:    
    def __init__(self, presion_arterial, temperatura, saturacion_o2, frecuencia_respiratoria, notas_evaluacion, imagenes_diagnosticas, resultados_laboratorio):     
        self.presion_arterial=presion_arterial
        self.temperatura=temperatura
        self.saturacion_o2=saturacion_o2
        self.frecuencia_respiratoria=frecuencia_respiratoria
        self.notas_evaluacion=notas_evaluacion
        self.imagenes_diagnosticas=imagenes_diagnosticas
        self.resultados_laboratorio=resultados_laboratorio
        self.medicamentos_formulados = []    
    
    def agregar_medicamento(self, medicamento):
        self.medicamentos_formulados.append(medicamento)

    def mostrar_historia_clinica(self):        
        print(f"Presión Arterial: {self.presion_arterial}")
        print(f"Temperatura: {self.temperatura}")
        print(f"Saturación O2: {self.saturacion_o2}")
        print(f"Frecuencia Respiratoria: {self.frecuencia_respiratoria}")
        print(f"Notas de evaluacion: {self.notas_evaluacion}")
        print(f"Imagen diagnostica: {self.imagenes_diagnosticas}")
        print(f"Resultados de laboratorio: {self.resultados_laboratorio}")
        print("Medicamentos Formulados:")
        for medicamento in self.medicamentos_formulados:
            print(f"Nombre: {medicamento.nombre}, Dosis: {medicamento.dosis}, Frecuencia: {medicamento.frecuencia}")
