#!/usr/bin/python3
# Desafio1.  Encontrar la sumatoria de todos los multiplos de 3 y de 5 
# inferiores a 1000

limite = int(input("Indique el limite para realizar el calculo: "))
secuencia = 0
multiplo = 0
suma = 0

while secuencia < limite - 1:
    
    secuencia = secuencia + 1
    print("la secuencia va en: ", secuencia)
    previo = multiplo
    print("el multiplo previo fue: ", previo)
 
    if secuencia%3 == 0 or secuencia%5 == 0:
        multiplo = secuencia
        suma = suma + multiplo
        print("el multiplo es", multiplo)
    
print("el resultado es", suma)
