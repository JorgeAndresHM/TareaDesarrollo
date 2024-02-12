class Paciente:

    lista_pacientes = []

    def __init__(self, documento, nombre, sexo, fecha_nacimiento):
        self.documento = documento
        self.nombre = nombre
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.historia_clinica = None
        Paciente.lista_pacientes.append(self)

    def asignar_historia_clinica(self, historia_clinica):
        self.historia_clinica = historia_clinica


    @classmethod
    def buscar_paciente_por_documento(cls, documento):
        for paciente in cls.lista_pacientes:
            if paciente.documento == documento:
                return paciente
        return None
    
    @classmethod
    def eliminar_paciente_por_documento(cls, documento):
        for paciente in cls.lista_pacientes:
            if paciente.documento==documento:
                cls.lista_pacientes.remove(paciente)                
                return True        
        return False


    