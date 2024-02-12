import os
import time

# Importar las clases
from Paciente import Paciente
from HistoriaClinica import HistoriaClinica
from Cama import Cama
from Medicamentos import Medicamentos

# lista de usuarios y contraseñas
usuarios = ["usuario1", "usuario2", "usuario3"]
contrasenias = ["contraseña1", "contraseña2", "contraseña3"]
cantidad_admisiones = 0
cantidad_altas = 0
cantidad_enfermedades_cronicas = 0

# Función para el inicio de sesión
def iniciar_sesion(usuario, contrasena):
    # Verificar si el usuario y la contraseña coinciden con los datos almacenados
    if usuario in usuarios and contrasena in contrasenias:
        print("Inicio de sesión exitoso.")
        time.sleep(1)
        # Llamar a la función para mostrar el menú
        abrir_menu()

    else:
        print("Inicio de sesión fallido. Usuario o contraseña incorrectos.")


# Funcion para abrir el menu principal
def abrir_menu():
    global cantidad_altas
    limpiar_consola()

    # Título del menú
    titulo = "GESTION HOSPITALARIA"
    imprimir_animacion(f"\n\n\t\t\t\t\t{titulo}\n\n")

    # Imprimir línea superior de la tabla
    imprimir_animacion("\t\t\t\t\t--" + "-" * 30 + "--\n")

    # Opciones del menú
    opciones = [
        "1. Ingresar historial clinico",
        "2. Buscar pacientes",
        "3. Eliminar pacientes",
        "4. Generar reporte",
        "5. Salir",
    ]

    # Imprimir opciones con animación y bordes
    for opcion in opciones:
        imprimir_animacion(f"\t\t\t\t\t| {opcion.ljust(31)}|\n")

    # Imprimir línea inferior de la tabla
    imprimir_animacion("\t\t\t\t\t--" + "-" * 30 + "--\n")

    imprimir_animacion("\t\t\t\t\tEscoge una opcion (1-5): ")
    opcion_escogida = input()
    if opcion_escogida == "1":
        ingresar_paciente()
    elif opcion_escogida == "2":
        # Solicitar el documento del paciente
        documento_paciente_buscar = input(
            "Ingrese el documento del paciente que desea buscar: "
        )

        # Buscar paciente por documento
        paciente_encontrado = Paciente.buscar_paciente_por_documento(
            documento_paciente_buscar
        )

        # Mostrar datos si se encontró el paciente
        if paciente_encontrado:
            limpiar_consola()
            imprimir_animacion("-" * 40)
            imprimir_animacion("\nDatos del paciente encontrado:\n")
            imprimir_animacion(f"Documento: {paciente_encontrado.documento}\n")
            imprimir_animacion(f"Nombre: {paciente_encontrado.nombre}\n")
            imprimir_animacion(f"Sexo: {paciente_encontrado.sexo}\n")
            imprimir_animacion(
                f"Fecha de Nacimiento: {paciente_encontrado.fecha_nacimiento}\n"
            )
            imprimir_animacion("Historia Clínica:\n")
            if paciente_encontrado.historia_clinica:
                paciente_encontrado.historia_clinica.mostrar_historia_clinica()
            else:
                imprimir_animacion("No hay historia clínica disponible.\n")
            imprimir_animacion("-" * 40)
        else:
            imprimir_animacion(
                f"No se encontró un paciente con el documento {documento_paciente_buscar}.\n"
            )

        opcion = input("\nDesea volver al menu? (Sí: 's' / No: presione Enter): ")
        if opcion.lower() == "s":
            abrir_menu()
    elif opcion_escogida == "3":
        limpiar_consola()
        # Solicitar el documento del paciente a eliminar
        documento_paciente_eliminar = input(
            "Ingrese el documento del paciente que desea eliminar: "
        )
        paciente_eliminado = Paciente.eliminar_paciente_por_documento(
            documento_paciente_eliminar
        )
        if paciente_eliminado:
            imprimir_animacion("Paciente eliminado con exito")
            cantidad_altas += 1
            Cama.cantidad_camas += 1
        else:
            imprimir_animacion(
                f"No se encontro un paciente con el documento {documento_paciente_eliminar}"
            )

        opcion = input("\nDesea volver al menu? (Sí: 's' / No: presione Enter): ")
        if opcion.lower() == "s":
            abrir_menu()

    elif opcion_escogida == "4":
        limpiar_consola()
        imprimir_animacion("-" * 35)
        imprimir_animacion(f"\nCantidad de admisiones: {cantidad_admisiones}\n")
        imprimir_animacion("-" * 35)
        imprimir_animacion(f"\nCantidad de altas: {cantidad_altas}\n")
        imprimir_animacion("-" * 35)
        imprimir_animacion(f"\nCantidad de camas disponibles: {Cama.cantidad_camas}\n")
        imprimir_animacion("-" * 35)
        imprimir_animacion(
            f"\nCantidad de enfermedades cronicas: {cantidad_enfermedades_cronicas}\n"
        )
        imprimir_animacion("-" * 35)

    else:
        imprimir_animacion("Programa Finalizado")


def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


def imprimir_animacion(texto):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.01)


# Función para la interfaz de inicio de sesión animada
def interfaz_inicio_sesion_animada():
    limpiar_consola()
    imprimir_animacion("INICIO DE SESION\n")

    usuario = input("USUARIO --> ")
    contrasena = input("CONTRASEÑA --> ")

    # Limpiar la consola y volver a imprimir la interfaz
    limpiar_consola()
    imprimir_animacion("INICIO DE SESION\n")
    imprimir_animacion(f"USUARIO --> {usuario}\n")
    imprimir_animacion(f"CONTRASEÑA --> {'*' * len(contrasena)}\n")

    # Llamar a la función de inicio de sesión con los datos ingresados
    iniciar_sesion(usuario, contrasena)


def ingresar_paciente():
    global cantidad_admisiones, cantidad_enfermedades_cronicas
    while True:
        limpiar_consola()
        imprimir_animacion("------ Historia Clinica ------")

        # Datos del paciente
        print("")
        imprimir_animacion("- Datos del paciente")
        print("")
        documento_paciente = input("    - Documento: ")
        nombre_paciente = input("    - Nombre: ")
        sexo = input("    - Sexo: ")
        fecha_nacimiento = input("    - Fecha de nacimiento (YYYY-MM-DD): ")

        # Signos vitales
        print("")
        imprimir_animacion("- Signos vitales")
        print("")
        presion_arterial = input("    - Presion Arterial: ")
        temperatura = input("    - Temperatura: ")
        saturacion_o2 = input("    - Saturacion O2: ")
        frecuencia_respiratoria = input("    - Frecuencia respiratoria: ")

        print("")
        # Notas de evaluacion
        notas_evaluacion = input("- Notas de evaluacion: ")
        print("")
        # Imagenes diagnosticas
        imagenes_diagnosticas = input("- Imagenes diagnosticas: ")
        print("")
        # Resultados de laboratorio
        resultados_laboratorio = input(
            "- Resultados de laboratorio (Presenta enfermedad cronica? Escribir si/no): "
        )
        if resultados_laboratorio == "si":
            cantidad_enfermedades_cronicas += 1

        # Medicamentos formulados
        medicamentos_formulados = []
        print("")
        while True:
            nombre_medicamento = input(
                "- Nombre del medicamento (o presione Enter para terminar): "
            )
            if not nombre_medicamento:
                break

            dosis = input("- Dosis (mg): ")
            frecuencia = input("- Frecuencia (por dia): ")

            nuevo_medicamento = Medicamentos(nombre_medicamento, dosis, frecuencia)
            medicamentos_formulados.append(nuevo_medicamento)

        nueva_historia_clinica = HistoriaClinica(
            presion_arterial,
            temperatura,
            saturacion_o2,
            frecuencia_respiratoria,
            notas_evaluacion,
            imagenes_diagnosticas,
            resultados_laboratorio,
        )

        for medicamento in medicamentos_formulados:
            nueva_historia_clinica.agregar_medicamento(medicamento)

        Cama.cantidad_camas -= 1
        cantidad_admisiones += 1

        # Crear una instancia de Paciente con la información proporcionada
        nuevo_paciente = Paciente(
            documento_paciente, nombre_paciente, sexo, fecha_nacimiento
        )

        # Asignar la historia clínica al paciente
        nuevo_paciente.asignar_historia_clinica(nueva_historia_clinica)

        # Preguntar al usuario si desea ingresar otro paciente o regresar al menú
        opcion = input("Desea ingresar otro paciente? (Sí: 's' / No: presione Enter): ")
        if opcion.lower() != "s":
            break

    abrir_menu()


# Llamar a la función para la interfaz de inicio de sesión
interfaz_inicio_sesion_animada()
