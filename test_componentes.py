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


@pytest.mark.telemetry_files(source("components.py"))
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


@pytest.mark.telemetry_files(source("components.py"))
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


vec_exe3 = ["0000", "0011", "0101", "0110", "1001", "1010", "1100", "1111"]


@pytest.mark.telemetry_files(source("components.py"))
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


@pytest.mark.telemetry_files(source("components.py"))
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


@pytest.mark.telemetry_files(source("components.py"))
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
