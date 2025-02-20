# Calculadora Básica de Terminal
import math

# Función para sumar dos números
def suma(a, b):
    return a + b

# Función para dividir dos números
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"
    
# Funcion para obtener la raiz cuadrada de un número
def raiz_cuadrada(a):
    if a < 0:
        return f"Error: el numero debe ser positivo"
    return math.sqrt(a)


while True:
    print("\nCalculadora Básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Salir")

    opcion = input("Elige una opción (1-7): ")

    if opcion == "7":
        print("Saliendo de la calculadora...")
        break

    if opcion in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print("Resultado:", suma(num1, num2))
        elif opcion == "2":
            print("Resultado:", resta(num1, num2))
        elif opcion == "3":
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == "4":
            print("Resultado:", division(num1, num2))
        elif opcion == "5":
            print("Resultado:", potencia(num1, num2))

    elif opcion == "6":
        num = float(input("Ingresa el número: "))
        print("Resultado:", raiz_cuadrada(num))

    else:
        print("Opción no válida. Intenta de nuevo.")



# Función para restar dos números
# def restar(a, b):
#     pass

# Función para multiplicar dos números
# def multiplicar(a, b):
#     pass

# Función para dividir dos números
# def dividir(a, b):
#     pass

# Función principal que muestra el menú y maneja la lógica de la calculadora
# def main():
#     pass

# Punto de entrada del programa
# if __name__ == "__main__":
#     main()
