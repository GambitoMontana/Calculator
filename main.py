import os
import subprocess
from funcionesMiniCalculadora import suma, resta, mult, div, mod, poW
"""Calculadora"""

# Primer ejercicio:
print("\n--Programa que suma dos numeros--")
x1 = float(input("Digite un numero: "))
x2 = float(input("Digite un numero: "))
x3 = x1 + x2

print(f"La suma de los dos numero es: {x3:.2f}")
input("Presione Enter para continuar....")
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

print("\n--------------------------------------\n")

process = True
# Segunda parte del ejercicio:
print("--Calculadora--")
while process:
    print("Observa que operaciones estan disponibles y elige una para realizarla...."
                "\n(1) Sumar dos numeros" \
                "\n(2) Restar dos numeros" \
                "\n(3) Multiplicar dos numeros" \
                "\n(4) Dividir dos numeros" \
                "\n(5) Obtener el residuo de dos numeros")
    option = int(input("\n-- Seleccione una opcion: "))
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    if option < 1 or option > 5:
        print("Opción incorrecta, intenta de nuevo.")
        input("\nPresione Enter para continuar...")
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
        continue

    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

# Verificar si se ingresaron valores validos o no...
    while process:
        try:
            n1 = float(input("\n- Digite el primer numero: "))
            n2 = float(input("- Digite el segundo numero: "))
            process = False
        except ValueError:
            print("Error al ingresar uno o mas valores, favor de intentar nuevamente....")

    process = True
    match option:
        case 1:
            print(f"El resultado de la suma es: ",suma(n1,n2))
        case 2:
            print(f"El resultado de la resta es: ",resta(n1,n2))
        case 3:
            print(f"El resultado de la multiplicacion es: ",mult(n1,n2))
        case 4:
            print(f"El resultado de la division es: ",div(n1,n2))
        case 5:
            print(f"El residuo de la operacion es: ",mod(n1,n2))
        case _:
            print("opcion incorrecta.....")

    closeProgram = int(input("\nSeleccione una ocpio:" \
    "\n(1) Realizar otra operacion" \
    "\n(2) Salir del programa" \
    "\n-- Opcion: "))

    if closeProgram == 2:
        print("Fin del programa....")
        process = False
    
    if closeProgram < 1 or closeProgram > 2:
        print("Opción incorrecta, intenta de nuevo.")
        input("\nPresione Enter para continuar...")
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
        continue
