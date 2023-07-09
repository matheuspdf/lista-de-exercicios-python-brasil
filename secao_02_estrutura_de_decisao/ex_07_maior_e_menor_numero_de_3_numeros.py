"""
Exercício 07 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior e o menor deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    Maior: 5
    Menor: 2
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    Maior: -1
    Menor: -10
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    Maior: 3
    Menor: -5
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    Maior: 15
    Menor: -14
"""


def calcular_maior_de_3_numeros(x, y, z):
    if x >= y and x >= z:
        maior = x
    elif y >= x and y >= z:
        maior = y
    else:
        maior = z

    if x <= y and x <= z:
        menor = x
    elif y <= x and y <= z:
        menor = y
    else:
        menor = z
    print(f'Maior: {maior}\nMenor: {menor}')


# Alternativa:
# def calcular_maior_de_3_numeros(x, y, z):
#     lista_de_numeros = [x, y, z]
#     maior = max(lista_de_numeros)
#     menor = min(lista_de_numeros)
#     print(f'Maior: {maior}\nMenor: {menor}')
