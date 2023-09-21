#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from myhdl import *
from .componentes import *

vec_exe1 = ["1101", "1111", "1001", "1101", "0000", "0010", "1010"]


def test_exe1():
    @instance
    def stimulus():
        for t in vec_exe1:
            x1.next = int(t[0])
            x2.next = int(t[1])
            x3.next = int(t[2])
            yield delay(1)
            assert z == int(t[3])

    x1, x2, x3, z = [Signal(bool(0)) for i in range(4)]
    dut = exe1(x1, x2, x3, z)
    sim = Simulation(dut, stimulus)
    sim.run()


vec_exe3 = ["0000", "0011", "0101", "0110", "1001", "1010", "1100", "1111"]


def test_exe3():
    @instance
    def stimulus():
        for t in vec_exe3:
            x3.next = int(t[0])
            x2.next = int(t[1])
            x1.next = int(t[2])

            yield delay(1)
            assert p == int(t[3])

    x3, x2, x1, p = [Signal(bool(0)) for i in range(4)]
    dut = exe3(x3, x2, x1, p)
    sim = Simulation(dut, stimulus)
    sim.run()


def test_add3():
    @instance
    def stimulus():
        for i in range(8):
            a.next = i
            yield delay(1)
            if a <= 4:
                assert b == i
            else:
                assert b == i + 3

    a = Signal(modbv(0)[4:])
    b = Signal(modbv(0)[4:])

    dut = add3(a, b)
    sim = Simulation(dut, stimulus)
    sim.run()


def test_exe4():
    @instance
    def stimulus():
        for i in range(64):
            b.next = i
            yield delay(1)
            bcd = "0" + str(int(b))
            high = bcd[-2]
            low = bcd[-1]
            assert int(p(8, 4)) == int(high)
            assert int(p(4, 0)) == int(low)

    b = Signal(modbv(0)[6:])
    p = Signal(modbv(0)[8:])

    dut = exe4(b, p)
    sim = Simulation(dut, stimulus)
    sim.run()
