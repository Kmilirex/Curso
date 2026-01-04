#Encontrar el numero mas grande de una serie de numeros dada por el usuario, e imprimirlo.

#Aqui le pedimos al usuario los 3 numeros.
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

#Verificamos si los tres numeros son iguales.
if numero1 == numero2 and numero1 == numero3:
    print("Todos los numeros son iguales")

#Comprobamos que numero es mayor y se imprime de una vez
elif numero1 >= numero2 and numero1 > numero3:
    print(f"El numero mayor es {numero1}")

elif numero2 >= numero1 and numero2 > numero3:
    print(f"El numero mayor es {numero2}")

else:
    print(f"El numero mayor es {numero3}")



