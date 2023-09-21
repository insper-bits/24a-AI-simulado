#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


from myhdl import *
from .exe2_extra import *


def exe1(x1, x2, x3, z):
    @always_comb
    def comb():
        z.next = 0

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
