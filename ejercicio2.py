# Función para determinar si una persona puede votar

# Crea una función llamada:puede_votar(edad)

# La función debe:

# Recibir la edad de una persona

# Si la edad es mayor o igual a 18, retornar "Puede votar"

# Si no, retornar "No puede votar"

# El programa principal debe:

# a. Pedir el nombre

# b. Pedir la edad

# c. Llamar a la función

# d. Mostrar el resultado en pantalla.

def puede_votar(edad):
    if edad >= 18:
        return "Puede Votar"
    else:
        return "No puede votar"


nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))


print(f"{nombre} usted tiene: {edad} y {puede_votar(edad)}")

