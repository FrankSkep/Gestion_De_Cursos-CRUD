from BD.conexion import ConexionBD
import functions
from utilities import *

def menuPrincipal():
    continuar = True
    opciones = [1, 2, 3, 4]
    while (continuar):
        opcionCorrecta = False
        while (not opcionCorrecta):
            cls()
            print("================= MENU PRINCIPAL =================")
            print("1. Listar cursos")
            print("2. Registrar curso")
            print("3. Actualizar curso")
            print("4. Eliminar curso")
            print("5. Salir")
            print("==================================================")
            opcion = getInt("> Elija una opcion: ")

            # Verifica que se ingrese una opcion valida
            if opcion in opciones:
                opcionCorrecta = True
                ejecutarOpcion(opcion)
            elif opcion == 5:
                print("\n* Has salido. *\n")
                continuar = False
                break
            else:
                print("Opcion incorrecta, seleccione nuevamente")
            pause()

# Ejecuta acciones de la opcion recibida
def ejecutarOpcion(opc):
    bd = ConexionBD()

    if opc == 1:  # Listar cursos
        try:
            # Variable que recibe los cursos de la base de datos
            cursos = bd.listarCursos()
            if len(cursos) > 0:
                functions.mostrarCursos(cursos)
            else:
                print("No se encontraron cursos\n")
        except Exception as err:
            print("Ocurrio un error: ", err)

    elif opc == 2:  # Registrar curso
        curso = functions.pedirDatosRegistrar()
        try:
            bd.registrarCurso(curso)
        except Exception as err:
            print("Ocurrio un error: ", err)

    elif opc == 3:  # Actualizar curso
        try:
            cursos = bd.listarCursos()  # Guardar cursos en la variable cursos
            if len(cursos) > 0:
                curso = functions.pedirDatosActualizacion(cursos)
                if curso:
                    bd.actualizarCurso(curso)
                else:
                    print("Codigo de curso a actualizar no encontrado\n")
            else:
                print("No se encontraron cursos\n")
        except Exception as err:
            print("Ocurrio un errorr: ", err)

    elif opc == 4: # Eliminar curso
        try:
            cursos = bd.listarCursos()  # Guardar cursos en la variable cursos
            if len(cursos) > 0:
                codigoEliminar = functions.eliminacionCurso(cursos)
                if not (codigoEliminar == ""):
                    bd.eliminarCurso(codigoEliminar)
                else:
                    print("* Codigo no encontrado *\n")
            else:
                print("No se encontraron cursos\n")
        except Exception as err:
            print("Ocurrio un error: ", err)

    else:
        print("Opcion no valida")


# Funcion Menu Principal
menuPrincipal()
