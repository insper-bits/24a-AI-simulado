#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


def exe1(a, b, c, s):
    @always_comb
    def comb():
        s.next = (a and b and c) or (a and not b and not (not a and not c))

    return instances()


def exe2(L, M, H, LED_verde, LED_amarelo, LED_vermelho, LED_azul, LED_laranja):
    @always_comb
    def comb():
        if M and not L:  # falha sensor
            LED_laranja.next = 1
        elif H and (not L or not M):  # falha sensor
            LED_laranja.next = 1
        elif L and not M and not H:  # nivel verde
            LED_verde.next = 1
        elif L and M and not H:  # nivel amarelo
            LED_amarelo.next = 1
        elif L and M and H:  # nivel vermelho
            LED_vermelho.next = 1
        elif not L and not M and not H:
            LED_azul.next = 1

    return instances()


def exe4_half_sub(x, y, b, q):
    @always_comb
    def comb():
        pass


def exe4_full_sub(x, y, z, b, q):
    @always_comb
    def comb():
        pass


def exe4_sub3(v2, v1, v0, p2, p1, p0, q2, q1, q0):
    @always_comb
    def comb():
        pass

    return instances()
