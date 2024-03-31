import random
import time
import os
import keyboard

generador_activo = False

def generar_ip():
    global generador_activo
    while generador_activo:
        ip = '.'.join('\033[92m' + str(random.randint(0, 255)).zfill(3) + '\033[0m' for _ in range(4))
        print(ip)
        time.sleep(0.001)  # Genera aproximadamente 1000 IPs por segundo

def detener_generador():
    global generador_activo
    generador_activo = False

def iniciar_generador():
    global generador_activo
    os.system("cls" if os.name == "nt" else "clear")  # Limpiar la pantalla antes de imprimir el título
    print("\n" * 10)  # Agregar espacios en blanco
    print(" " * 30 + "\033[1m" + "Generador de ip programado por zazzy2" + "\033[0m")  # Título en letras grandes
    generador_activo = True
    generar_ip()

    keyboard.add_hotkey('space', detener_generador)
    while generador_activo:
        time.sleep(0.1)

    print("\nGenerador detenido.")

def iniciar_con_contraseña():
    while True:
        password = input("Introduce la contraseña para iniciar el generador: ")
        if password == "zazzyrich35":
            print("Contraseña correcta.")
            return True
        else:
            print("Contraseña incorrecta. Por favor, inténtalo de nuevo.")
    return False

def start_generator():
    global generador_activo
    if not generador_activo:
        iniciar_generador()
    else:
        print("El generador ya está en funcionamiento.")

if __name__ == "__main__":
    if iniciar_con_contraseña():
        print("Se ha iniciado el generador. Usa el comando '!start_generator' para comenzar el generador.")
        while True:
            command = input("Ingrese un comando ('!start_generator' para iniciar el generador o 'exit' para salir): ")
            if command == "!start_generator":
                start_generator()
            elif command == "exit":
                print("Saliendo del programa.")
                break
            else:
                print("Comando no reconocido.")
