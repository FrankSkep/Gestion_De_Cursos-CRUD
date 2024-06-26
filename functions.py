# ------- Funcion para mostrar cursos existentes -------
def mostrarCursos(cursos):
    print("\n\t\t\t> Cursos <\n")
    contador = 1  # Contador para enumerar cursos
    for curso in cursos:
        datos = "{0}. Codigo: {1} | Nombre: {2} ({3} Creditos)"
        print(datos.format(contador, curso[0], curso[1], curso[2]))
        contador += 1
    print(" ")


#------- Funcion para registrar un curso nuevo -------
def pedirDatosRegistrar():
    # Validar que ingrese un codigo correcto de 6 digitos
    codigoCorrecto = False
    while (not codigoCorrecto):
        codigo = input("> Ingresa codigo del curso: ")
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print("\n* Codigo incorrecto: el codigo debe tener 6 digitos *\n")

    # Pedir nombre del curso
    nombreCorrecto = False
    while (not nombreCorrecto):
        nombre = input("> Ingresa nombre del curso: ")
        if (nombre.isnumeric()):
            print("\n* Nombre no valido: Ingresa solo letras *")
        else:
            nombreCorrecto = True

    # Validar que ingrese un valor numerico en creditos
    creditosCorrectos = False
    while (not creditosCorrectos):
        creditos = input("> Ingresa creditos del curso: ")
        if creditos.isnumeric():
            if (int(creditos) > 0):
                creditosCorrectos = True
                creditos = int(creditos)
            else:
                print("\n* Creditos no validos: Los creditos deben ser mayor a 0 *\n")
        else:
            print("\n* Creditos no validos: Deben ser numeros unicamente *\n")
    # Guardar datos en una tupla
    curso = (codigo, nombre, creditos)
    return curso  # Retornar tupla con los datos ingresados


#------- Funcion para modificar un curso -------
def pedirDatosActualizacion(cursos):
    mostrarCursos(cursos)
    existeCodigo = False
    codigoEditar = input("> Ingrese codigo del curso a editar: ")
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        nombre = input("> Ingresa nuevo nombre: ")
        # Validar que ingrese un valor numerico en creditos
        creditosCorrectos = False
        while (not creditosCorrectos):
            creditos = input("> Ingresa nuevo valor en creditos: ")
            if creditos.isnumeric():
                if (int(creditos) > 0):
                    creditosCorrectos = True
                    creditos = int(creditos)
                else:
                    print(
                        "\n* Creditos no validos: Los creditos deben ser mayor a 0 *\n")
            else:
                print("\n* Creditos no validos: Deben ser numeros unicamente *\n")
        # Guardar datos actualizados en la tupla
        curso = (codigoEditar, nombre, creditos)
    else:
        curso = None
    return curso

#------- Funcion para eliminar un curso -------
def eliminacionCurso(cursos):
    mostrarCursos(cursos)  # Mostrar cursos

    existeCodigo = False
    codigoEliminar = input("> Ingrese codigo del curso a eliminar: ")
    for curso in cursos:
        # curso[0] ya que codigo es el primer elemento de la lista de cada curso
        if curso[0] == codigoEliminar:
            existeCodigo = True
            break

    # Si no existe el codigo ingresado
    if not existeCodigo:
        print("\n* Curso no existente: verifique el codigo ingresado. *\n")
        codigoEliminar = ""
    return codigoEliminar
