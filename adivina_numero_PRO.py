import random
import os

# 🛠 Asegurar que el archivo record_podio.txt se guarde junto al script
RUTA_BASE = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_PODIO = os.path.join(RUTA_BASE, "record_podio.txt")

def cargar_podio():
    podio = []
    if os.path.exists(ARCHIVO_PODIO):
        with open(ARCHIVO_PODIO, "r") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) == 2 and partes[0].isdigit():
                    podio.append((int(partes[0]), partes[1]))
    return sorted(podio)[:3]

def guardar_podio(podio):
    with open(ARCHIVO_PODIO, "w") as f:
        for intentos, nombre in podio:
            f.write(f"{intentos},{nombre}\n")

def mostrar_podio(podio):
    print("\n🏆 PODIO - Mejores 3 Marcas 🏆")
    medallas = ['🥇', '🥈', '🥉']
    if not podio:
        print("Aún no hay récords registrados.")
    else:
        for i, (intentos, nombre) in enumerate(podio):
            print(f"{i+1}. {nombre} - {intentos} intento(s) {medallas[i]}")
    print()

def jugar(podio, modo_estricto=True):
    numero = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            intento = int(input("Adivina un número del 1 al 100: "))

            if intento < 1 or intento > 100:
                print("El número debe estar entre 1 y 100.")
                if modo_estricto:
                    intentos += 1
                continue

            intentos += 1

            if intento > numero:
                print("El número fue muy alto.")
            elif intento < numero:
                print("El número fue muy bajo.")
            else:
                print(f"🎯 ¡Correcto! El número era {intento}. Lo lograste en {intentos} intentos.")

                if len(podio) < 3 or intentos < podio[-1][0]:
                    print("¡Felicitaciones! Entraste al podio 🏆")
                    while True:
                        nombre = input("Ingresá tu nombre/código (3 caracteres exactos): ")
                        if len(nombre) == 3:
                            break
                        else:
                            print("Debe tener exactamente 3 caracteres.")
                    podio.append((intentos, nombre))
                    podio.sort()
                    podio[:] = podio[:3]
                    guardar_podio(podio)
                else:
                    print("Buen intento, pero no alcanzó para entrar al podio.")
                break
        except ValueError:
            print("Eso no es un número válido.")

def menu_principal():
    podio = cargar_podio()

    while True:
        print("\n🎮 JUEGO: ADIVINA EL NÚMERO 🎮")
        print("1. Jugar (modo estricto: cuenta todo intento)")
        print("2. Jugar (modo flexible: solo cuenta intentos válidos)")
        print("3. Ver récords")
        print("4. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            jugar(podio, modo_estricto=True)
        elif opcion == "2":
            jugar(podio, modo_estricto=False)
        elif opcion == "3":
            mostrar_podio(podio)
        elif opcion == "4":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción inválida. Intentá de nuevo.")

menu_principal()
