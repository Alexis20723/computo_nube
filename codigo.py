def es_primo(numero):
    """Verifica si un número es primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

if __name__ == "__main__":
    # Programa principal
    try:
        # Obtener la entrada del usuario
        entrada_usuario = int(input("Ingresa un número entero: "))
        
        # Verificar si el número ingresado es primo
        if es_primo(entrada_usuario):
            print(f"{entrada_usuario} es un número primo.")
        else:
            print(f"{entrada_usuario} no es un número primo.")
    except ValueError:
        print("Por favor, ingresa un entero válido.")
        


def mediana_de_tres(num1, num2, num3):
    """Devuelve el valor mediano de tres números."""
    # Encontrar el valor intermedio
    if num1 <= num2 <= num3 or num3 <= num2 <= num1:
        return num2
    elif num2 <= num1 <= num3 or num3 <= num1 <= num2:
        return num1
    else:
        return num3

if __name__ == "__main__":
    try:
        # Obtener la entrada del usuario
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        num3 = float(input("Ingresa el tercer número: "))

        # Calcular y mostrar la mediana
        resultado = mediana_de_tres(num1, num2, num3)
        print(f"La mediana de {num1}, {num2} y {num3} es {resultado}.")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")


import random

def generar_contraseña_aleatoria():
    """Genera una contraseña aleatoria."""
    longitud_contraseña = random.randint(7, 10)
    contraseña = ''.join(chr(random.randint(33, 126)) for _ in range(longitud_contraseña))
    return contraseña

if __name__ == "__main__":
    # Muestra la contraseña generada aleatoriamente
    contraseña_aleatoria = generar_contraseña_aleatoria()
    print(f"Contraseña generada aleatoriamente: {contraseña_aleatoria}")
    
    
    
    

def calcular_hipotenusa(lado1, lado2):
    """Calcula la hipotenusa de un triángulo rectángulo."""
    hipotenusa = (lado1**2 + lado2**2)**0.5
    return hipotenusa

if __name__ == "__main__":
    try:
        # Obtener la entrada del usuario para las longitudes de los lados más cortos
        lado_corto1 = float(input("Ingresa la longitud del primer lado más corto: "))
        lado_corto2 = float(input("Ingresa la longitud del segundo lado más corto: "))

        # Calcular la hipotenusa usando la función
        resultado = calcular_hipotenusa(lado_corto1, lado_corto2)

        # Mostrar el resultado
        print(f"La hipotenusa del triángulo rectángulo es: {resultado}")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

