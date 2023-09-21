#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


from myhdl import *
from .exe2_extra import *


def exe1(a, b, c, s):
    @always_comb
    def comb():
        s.next = (a and b and c) or (a and not b and not(not a and not c))

    return instances()



def exe2(L, M, H, LED_verde, LED_amarelo, LED_vermelho, LED_azul, LED_laranja):
    LED_verde.next = 0
    LED_amarelo.next = 0
    LED_vermelho.next = 0
    LED_azul.next = 0
    LED_laranja.next = 0

    @always_comb
    def comb():
        if M and not L:   # falha sensor
            LED_laranja.next = 1
        elif H and (not L or not M): # falha sensor
            LED_laranja.next = 1
        elif L and not M and not H:  # nivel verde
            LED_verde.next = 1
        elif L and M and not H: # nivel amarelo
            LED_amarelo.next = 1
        elif L and M and H:  # nivel vermelho
            LED_vermelho.next = 1
        elif not L and not M and not H:
            LED_azul.next = 1

    return instances()










def exe3(x3, x2, x1, p):
    @always_comb
    def comb():
        p.next = 0

    return instances()


def exe4(b, p):

    # tip:
    # vc vai precisar usar essas variáveis auxiliares
    # que sao as saidas dos add3
    add3_1_out, add3_2_out, add3_3_out = [Signal(modbv(0)[4:]) for i in range(3)]

    # tip:
    # vai ter que usar concatsignal para as entradas
    # dos somadores (criando um novo vetor)
    # exemplo para o primeiro
    add3_1_in = ConcatSignal(False, b(5), b(4), b(3))

    # tip:
    # agora vc deve utilizar os componentes
    # c1_add3 = ...
    # c2_add3 = ...

    @always_comb
    def comb():
        # tip: lembre de atualizar a saída
        # p.next[0] = b(0)
        # ...
        pass

    return instances()


def add3(a, b):
    @always_comb
    def comb():
        b.next = 0

    return instances()
