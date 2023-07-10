"""
Exercício 09 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre-os em ordem decrescente.

    >>> ordenar_decrescente(2, 3, 5)
    5, 3, 2
    >>> ordenar_decrescente(10, 5.55, 7)
    10, 7, 5.55
    >>> ordenar_decrescente(20, 30, 17.62)
    30, 20, 17.62
    >>> ordenar_decrescente(7, 1, 15)
    15, 7, 1

"""


def ordenar_decrescente(x, y, z):
    if x >= y and x >= z:
        maior = x
        if y >= z:
            meio = y
            menor = z
        else:
            meio = z
            menor = y
    if y >= x and y >= z:
        maior = y
        if x >= z:
            meio = x
            menor = z
        else:
            meio = z
            menor = x
    if z >= y and z >= x:
        maior = z
        if y >= x:
            meio = y
            menor = x
        else:
            meio = x
            menor = y
    print(f'{maior}, {meio}, {menor}')


# Alternativa:
# def ordenar_decrescente(x, y, z):
#     numeros = [x, y, z]
#     ordem_decrescente = sorted(numeros, reverse=True)
#     print(f'{ordem_decrescente[0]}, {ordem_decrescente[1]}, {ordem_decrescente[2]}')
