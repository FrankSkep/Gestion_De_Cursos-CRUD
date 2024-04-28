from BD.conexion import ConexionBD
import functions


def menuPrincipal():
    continuar = True
    # Bucle while para repetir menu mientras no seleccione 'salir'
    while (continuar):
        opcionCorrecta = False
        while (not opcionCorrecta):
            print("================= MENU PRINCIPAL =================")
            print("1. Listar cursos")
            print("2. Registrar curso")
            print("3. Actualizar curso")
            print("4. Eliminar curso")
            print("5. Salir")
            print("==================================================")
            opcion = int(input("Seleccione una opcion: "))

        # Verifica que se ingrese una opcion valida
            if opcion < 1 or opcion > 5:
                print("Opcion incorrecta, seleccione nuevamente")
            elif opcion == 5:
                print("\nHas salido, gracias por usar este sistema.\n")
                continuar = False
                opcionCorrecta = True
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

# Funcion para ejecutar la opcion elegida


def ejecutarOpcion(opc):
    bd = ConexionBD()

    # Opcion Listar cursos
    if opc == 1:
        try:
            # Variable que recibe los cursos de la base de datos
            cursos = bd.listarCursos()
            if len(cursos) > 0:
                functions.mostrarCursos(cursos)
            else:
                print("No se encontraron cursos\n")
        except Exception as err:
            print("Ocurrio un error: ", err)

    # Opcion Registrar curso
    elif opc == 2:
        curso = functions.pedirDatosRegistrar()
        try:
            bd.registrarCurso(curso)
        except Exception as err:
            print("Ocurrio un error: ", err)

    # Opcion Actualizar curso
    elif opc == 3:
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

    # Opcion Eliminar curso
    elif opc == 4:
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
