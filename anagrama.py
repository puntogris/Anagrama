#!/usr/bin/env python3
# Anagrama
# dada una palabra busca anagramas de la misma
print('Ingrese una palabra para buscar:')
palabra = input()
listapalabras = "palabras.txt"
f = open(listapalabras, 'r')
lines = f.readlines()

for line in lines:
    if sorted(list(line)[:-1]) == sorted(palabra):
        print(line.replace("\n", " "))
f.close()
