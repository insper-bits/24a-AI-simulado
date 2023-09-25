#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from myhdl import *
from componentes import *
import pytest
import os

try:
    from telemetry import telemetryMark

    pytestmark = telemetryMark()
except ImportError as err:
    print("Telemetry não importado")


def source(name):
    dir = os.path.dirname(__file__)
    src_dir = os.path.join(dir, ".")
    return os.path.join(src_dir, name)


vec_exe1 = ["0000", "0010", "0100", "0110", "1001", "1011", "1100", "1111"]


@pytest.mark.telemetry_files(source("componentes.py"))
def test_exe1():
    @instance
    def stimulus():
        for t in vec_exe1:
            a.next = int(t[0])
            b.next = int(t[1])
            c.next = int(t[2])
            yield delay(1)
            assert s == int(t[3])

    a, b, c, s = [Signal(bool(0)) for i in range(4)]
    dut = exe1(a, b, c, s)
    sim = Simulation(dut, stimulus)
    sim.run()


vec_exe2 = [
    "00000010",
    "00100001",
    "01000001",
    "01100001",
    "10010000",
    "10100001",
    "11001000",
    "11100100",
]


@pytest.mark.telemetry_files(source("componentes.py"))
def test_exe2():
    @instance
    def stimulus():
        for t in vec_exe1:
            L.next = int(t[0])
            M.next = int(t[1])
            H.next = int(t[2])
            yield delay(1)
            assert LED_verde == int(t[3])
            assert LED_amarelo == int(t[4])
            assert LED_vermelho == int(t[5])
            assert LED_azul == int(t[6])
            assert LED_laranja == int(t[7])

    a, b, c, s = [Signal(bool(0)) for i in range(4)]
    dut = exe2(L, M, H, LED_verde, LED_amarelo, LED_vermelho, LED_azul, LED_laranja)
    sim = Simulation(dut, stimulus)
    sim.run()


vec_exe3 = ["0001001", "0011011", "0101101", "1110111"]

@pytest.mark.telemetry_files(source("componentes.py"))
def test_exe3():
    @instance
    def stimulus():
        t = "0000"
        i3.next = int(t[3])
        i2.next = int(t[2])
        i1.next = int(t[1])
        i0.next = int(t[0])
        yield delay(1)
        assert v == 0

        for test in vec_exe3:
            print(test)
            i3.next = int(test[0])
            i2.next = int(test[1])
            i1.next = int(test[2])
            i0.next = int(test[3])

            yield delay(1)
            assert int(p1) == int(test[4])
            assert int(p0) == int(test[5])
            assert int(v) == int(test[6])

    i3, i2, i1, i0, p1, p0, v = [Signal(bool(0)) for i in range(7)]
    dut = exe3(i3, i2, i1, i0, p1, p0, v)
    sim = Simulation(dut, stimulus)
    sim.run()

vec_exe4_half = ["0000", "0111", "1001", "1100"]

@pytest.mark.telemetry_files(source("componentes.py"))
def test_exe4_half():
    @instance
    def stimulus():
        for test in vec_exe4_half:
            x.next = int(test[0])
            y.next = int(test[1])
            yield delay(1)
            assert int(b) == int(test[2])
            assert int(d) == int(test[3])

    x,y,b,d= [Signal(bool(0)) for i in range(4)]
    dut = exe4_half_sub(x,y,b,d)
    sim = Simulation(dut, stimulus)
    sim.run()
