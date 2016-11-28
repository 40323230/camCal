# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from .canvas import chart
from .formula import *

class Harmonic():
    def __init__(self):
        #H
        self.H = chart()
        path, rate, findMax = Har_H()
        self.H.setPath(path)
        self.H.setRate(rate)
        self.H.setColor(Qt.blue)
        self.H.setMaxima(findMax)
        self.H.setFormula("ΔR = (H/2)*[1-cos(π*t/T)]\nΔR = (H/2)*[1-cos(π*φ/β)]")
        #velocity
        self.velocity = chart()
        path, rate, findMax = Har_velocity()
        self.velocity.setPath(path)
        self.velocity.setRate(rate)
        self.velocity.setColor(Qt.green)
        self.velocity.setMaxima(findMax)
        self.velocity.setFormula("v = [(π*H)/(2*T)]*sin(π*t/T)\nv = [(π*H*ω)/(2*β)]*sin(π*φ/β)")
        #acceleration
        self.acceleration = chart()
        path, rate, findMax = Har_acceleration()
        self.acceleration.setPath(path)
        self.acceleration.setRate(rate)
        self.acceleration.setColor(Qt.cyan)
        self.acceleration.setMaxima(findMax)
        self.acceleration.setFormula("a = [(π^2*H)/(2*T^2)]*cos(π*t/T)\na = [(π^2*H*ω^2)/(2*β^2)]*cos(π*φ/β)")
        #jump
        self.jump = chart()
        path, rate, findMax = Har_jump()
        self.jump.setPath(path)
        self.jump.setRate(rate)
        self.jump.setColor(QColor(225, 165, 0))
        self.jump.setMaxima(findMax)
        self.jump.setFormula("j = [(π*H)/(2*T)]*sin(π*t/T)\nj = [(π*H)/(2*β)]*sin(π*φ/β)")

class Cycloidal():
    def __init__(self):
        #H
        self.H = chart()
        path, rate, findMax = Cy_H()
        self.H.setPath(path)
        self.H.setRate(rate)
        self.H.setColor(Qt.blue)
        self.H.setMaxima(findMax)
        self.H.setFormula("ΔR = (H*t/T)-(H/2*π)*sin(2*π*t/T)\nΔR = (H*φ/β)-(H/2*π)*sin(2*π*φ/β)")
        #velocity
        self.velocity = chart()
        path, rate, findMax = Cy_velocity()
        self.velocity.setPath(path)
        self.velocity.setRate(rate)
        self.velocity.setColor(Qt.green)
        self.velocity.setMaxima(findMax)
        self.velocity.setFormula("v = H-H*cos(2*π*t/T)\nv = H-H*cos(2*π*φ/β)")
        #acceleration
        self.acceleration = chart()
        path, rate, findMax = Cy_acceleration()
        self.acceleration.setPath(path)
        self.acceleration.setRate(rate)
        self.acceleration.setColor(Qt.cyan)
        self.acceleration.setMaxima(findMax)
        self.acceleration.setFormula("a = H*π*2*sin(2*π*t/T)\na = H*π*2*sin(2*π*φ/β)")
        #jump
        self.jump = chart()
        path, rate, findMax = Cy_jump()
        self.jump.setPath(path)
        self.jump.setRate(rate)
        self.jump.setColor(QColor(225, 165, 0))
        self.jump.setMaxima(findMax)
        self.jump.setFormula("j = H*π^2*4*cos(2*π*t/T)\nj = H*π^2*4*cos(2*π*φ/β)")
