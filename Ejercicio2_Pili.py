# 1: Pidele al usuario que ingrese dos numeros enteros por teclado
# y determine los siguientes aspectos.

num_1 = int(input("Ingrese un entero para el número 1: "))
num_2 = int(input("Ingrese un entero para el número 2: "))

# a: Si ambos numeros son iguales
print(num_1 == num_2)

# b: Si los numeros son diferentes
print(num_1 != num_2)

# c: Si el primero  es mayor al segundo
print(num_1 > num_2)

# d: Si el segundo es mayor al primero
print(num_1 < num_2)

# 2: Determina que el resultado tienen los siguientes ejemplos

print(not True) # False

print(True and True) # True

print(not False) # True

print(False or True) # True

# 3: Con operadores logicos, determina si una cadena de texto ingresada por el usuario
# tiene una longitud mayor o igual a 3 y a su vez es menor a 10. (true o false)

c = input("Ingrese una cadena: ")

print(len(c) >= 3 and len(c) <= 10)

# 4: Crea una variable y asignale un valor entero. Pidele al usuario un numero por teclado, crea una variable usuario,
# a la misma variable asignale una multiplicacion por 9. 
# Luego multiplica en asignacion la primer variable con la segunda e imprime
# en pantalla el resultado.

a = 20
print("El valor de a es: " + str(a))
b = int(input("Ingrese un número entero: "))
b *= 9
print("El valor de b*9 es: " + str(b))

a *= b

print("El valor de a*b es: " + str(a))
