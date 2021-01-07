""" (1)Escribir un programa que almacene la cadena de caracteres contraseña en una 
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña 
correcta. """

password = "9832"

pw = input("Ingrese la contraseña: ")
while password != pw:
    pw = input("Ingrese la contraseña: ")
print("Welcome to de Jungle")

""" (2) Escribir un programa que pida al usuario una palabra y la muestre por pantalla 
10 veces. """

word = input("Ingrese una palabra: ")
for i in range(10) :
    print(word)

""" (3) Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
los años que ha cumplido (desde 1 hasta su edad). """

edad = input("Ingrese su edad: ")
for i in range(1, int(edad) + 1) :
    print(i)

""" (4)Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta 
que el usuario escriba 'salir' que terminará. """

while True:
    c = input("Ingrese cualquier palabra, si desea finalizar ingrese Salir: ")
    print(c)
    if (c == "Salir"):
        break

""" (5)Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos 
ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al 
usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que 
tributar o no. """

edad = int(input("Ingrese su edad: "))
ingreso = int(input("Ingrese su ingresos mensuales: "))

if (edad > 16 and ingreso >= 1000):
    print("Usted debe tributar")
else: 
    print("Usted NO debe Tributar")

