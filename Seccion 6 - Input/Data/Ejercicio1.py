from math import sqrt

valorA = int(input("Introduce el valor de a: "))
valorB = int(input("Introduce el valor de b: "))
valorC = int(input("Introduce el valor de c: "))
ValorX1 = (-valorB + sqrt((valorB**2)- (4* valorA * valorC))) / (2 * valorA)
ValorX2 = (-valorB - sqrt((valorB**2)- (4* valorA * valorC))) / (2 * valorA)

print("La slución es: \nX1=",ValorX1, "\nX2=" ,ValorX2)