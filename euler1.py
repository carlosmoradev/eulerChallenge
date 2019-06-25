#!/usr/bin/python3

limite = int(input("Indique el limite para realizar el calculo: "))
secuencia = 0
multiplo = 0
suma = 0

while secuencia < limite - 1:
    
    secuencia = secuencia + 1
    print("la secuencia va en: ", secuencia)
    previo = multiplo
    print("el multiplo previo fue: ", previo)
    # if previo != multiplo:
    suma = multiplo + previo

    if secuencia%3 == 0 or secuencia%5 == 0:
        multiplo = secuencia
        # multiplo = multiplo + valor
        print("el multiplo es", multiplo)
    
print("el resultado es", suma)
