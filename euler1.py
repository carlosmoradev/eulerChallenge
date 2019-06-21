#!/usr/bin/python3

limite = int(input("Indique el limite para realizar el calculo: "))
secuencia = 1
multiplo = 0
suma = 0

while secuencia < limite - 1:
    secuencia = secuencia + 1
    if secuencia%3 == 0 or secuencia%5 == 0:
        multiplo = secuencia
        print("el multiplo es", multiplo)
    suma = multiplo + secuencia
        

print("el resultado es", suma)
