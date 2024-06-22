import os

# Limpia pantalla para cualquier sistema operativo
def cls() -> None:
    if os.name == 'nt':  # Si es Windows
        os.system('cls')
    else:  # Si es Unix/Linux/MacOS/BSD/etc
        os.system('clear')

# Pausa hasta que se presione enter
def pause() -> None:
    input("Presiona enter para continuar")

# Validar que se ingrese un valor numerico
def getInt(msg: str) -> int:
    while True:
        numero = input(msg)
        try:
            return int(numero)
        except:
            continue
