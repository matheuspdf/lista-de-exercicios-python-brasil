"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 galão(ões) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 galão(ões) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""
import math


def calcular_latas_e_preco_de_tinta():

    """Escreva aqui em baixo a sua solução"""

    # Entrada
    area_a_ser_pintada_em_m2 = float(input('Digite o tamanho da área a ser pintada em metros quadrados: '))

    # Calcular a quantidade de tinta necessária com 10% de folga
    quantidade_de_litros_necessarios = (area_a_ser_pintada_em_m2 / 6) * 1.1
    litros_arredondados_para_cima = math.ceil(quantidade_de_litros_necessarios)

    # Calcular a quantidade e o custo das latas de 18 litros
    quantidade_de_latas = math.ceil(litros_arredondados_para_cima / 18)
    custo_de_latas = quantidade_de_latas * 80
    sobra_latas = quantidade_de_latas * 18 - litros_arredondados_para_cima

    # Calcular a quantidade e o custo dos galões de 3,6 litros
    quantidade_de_galoes = math.ceil(litros_arredondados_para_cima / 3.6)
    custo_de_galoes = quantidade_de_galoes * 25
    sobra_galoes = quantidade_de_galoes * 3.6 - litros_arredondados_para_cima

    # Calcular a quantidade e o custo da combinação entre latas e galões
    latas = litros_arredondados_para_cima // 18
    restante = litros_arredondados_para_cima % 18
    galoes = math.ceil(restante / 3.6)
    custo_misto = latas * 80 + galoes * 25
    sobra_misto = latas * 18 + galoes * 3.6 - litros_arredondados_para_cima

    # Saída
    print(f'Você deve comprar {litros_arredondados_para_cima} litros de tinta.')
    print(
        f'Você pode comprar {quantidade_de_latas} lata(s) de 18 litros a um custo de R$ {custo_de_latas:}. Vão sobrar {sobra_latas:.1f} litro(s) de tinta.')
    print(
        f'Você pode comprar {quantidade_de_galoes} galão(ões) de 3.6 litros a um custo de R$ {custo_de_galoes:}. Vão sobrar {sobra_galoes:.1f} litro(s) de tinta.')
    print(
        f'Para menor custo, você pode comprar {latas} lata(s) de 18 litros e {galoes} galão(ões) de 3.6 litros a um custo de R$ {custo_misto:}. Vão sobrar {sobra_misto:.1f} litro(s) de tinta.')
