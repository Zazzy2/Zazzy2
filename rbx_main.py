import random
import string
import time
import os
import keyboard

generador_activo = False

def generar_codigo():
    global generador_activo
    while generador_activo:
        longitud = random.randint(8, 12)  # longitud aleatoria para cada código
        codigo = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(longitud))
        print(codigo)
        time.sleep(0.001)  # Genera aproximadamente 1000 códigos por segundo

def detener_generador():
    global generador_activo
    generador_activo = False

def main():
    global generador_activo
    os.system("cls")  # Limpiar la pantalla antes de imprimir el título
    print("\n" * 10)  # Agregar espacios en blanco
    print(" " * 30 + "\033[1m" + "Generador de robux programado por zazzy2" + "\033[0m")  # Título en letras grandes
    comando = input("\nEscribe .on para iniciar el comando: ")
    if comando == ".on":
        generador_activo = True
        generar_codigo()
    else:
        print("Comando no reconocido.")

    keyboard.add_hotkey('space', detener_generador)
    while generador_activo:
        time.sleep(0.1)

    print("\nGenerador detenido.")

if __name__ == "__main__":
    main()
