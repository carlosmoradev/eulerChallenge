#!/usr/bin/python3
#Desafio 2.  Encontrar la serie fibonacci para numeros inferiores a 4'000.000
total = 2
anterior = 1
nuevo = 0

def calculo(limite):
    if limite<=0:
        print("numero invalido")
    while total < limite:
        nuevo = total + anterior
        anterior = total
        total = nuevo

print(calculo(int(input("Ingrese el limite: "))))