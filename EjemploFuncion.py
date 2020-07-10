# escribir un programa que pida al usuario un texto y un numero entero.
# Mandar a imprimir en pantalla el texto repetido las veces indicado por 
# el numero. Nota: Hacer el programa usando una función
#
# Ingresa un texto: hola
# Ingresa un numero: 4
# Salida:
# hola
# hola
# hola
# hola
#  

# declarar la funcion
def repetir(texto, numero):
    texto += '\n'
    print(texto*numero)

# escribir el codigo para usar la funcion
t = input("Ingresa un texto ")
n = int(input("Ingresa un numero"))

repetir(t,n)


