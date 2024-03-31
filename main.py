import os
import time
import random
import string

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def generar_codigo():
    codigo = "https://discord.gift/" + "".join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    return codigo

def imprimir_azul(texto):
    print("\033[94m" + texto + "\033[0m")  # Imprimir en azul

def main():
    limpiar_pantalla()
    codigo = input("contraseÃ±a: ")
    if codigo.lower() == "zazzyrich35":
        limpiar_pantalla()
        imprimir_azul("NITRO GEN")
        print("\nMade by Zazzy2       ingresa .on para empezar")
        while True:
            opcion = input()
            if opcion == ".on":
                limpiar_pantalla()
                start_time = time.time()
                count = 0
                while True:
                    codigo_generado = generar_codigo()
                    imprimir_azul(codigo_generado)
                    count += 1
                    if count == 1000:
                        elapsed_time = time.time() - start_time
                        if elapsed_time < 1:
                            time.sleep(1 - elapsed_time)
                        start_time = time.time()
                        count = 0
            else:
                print("este comando no existe gay")
    else:
        print("si no te lo sabes no pongas nada,tonto.")

if __name__ == "__main__":
    main()
