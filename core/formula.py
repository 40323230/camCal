from math import cos, sin, pi
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

H = 25
T = 90

def Har_H():
    answer = []
    for t in range(0, 90):
        answer += [{'x':t, 'y':0}]
    for t in range(90, 180):
        y = (H/2)*(1-cos(pi*t/T))-H
        answer += [{'x':t, 'y':y}]
    for t in range(180, 270):
        answer += [{'x':t, 'y':-H}]
    for t in range(270, 360):
        y = (H/2)*(1+cos(pi*t/T))-H
        answer += [{'x':t, 'y':y}]
    findMax = []
    for i in range(0, 360):
        findMax += [H/2*(1-cos(2*i/180*pi))]
    return answer, 60, findMax

def Har_velocity():
    answer = []
    for t in range(0, 90):
        answer += [{'x':t, 'y':0}]
    for t in range(90, 180):
        y = ((pi*H)/(2*T))*sin(pi*t/T)
        answer += [{'x':t, 'y':y}]
    for t in range(180, 270):
        answer += [{'x':t, 'y':0}]
    for t in range(270, 360):
        y = ((pi*H)/(2*T))*sin(pi*t/T)*(-1)
        answer += [{'x':t, 'y':y}]
    findMax = []
    for i in range(0, 360):
        findMax += [2*pi*sin(2*i/180*pi)*H]
    return answer, 1, findMax

def Har_acceleration():
    answer = []
    for t in range(0, 90):
        answer += [{'x':t, 'y':0}]
    for t in range(90, 180):
        y = ((pi**2*H)/(2*T**2))*cos(pi*t/T)
        answer += [{'x':t, 'y':y}]
    for t in range(180, 270):
        answer += [{'x':t, 'y':0}]
    for t in range(270, 360):
        y = -((pi**2*H)/(2*T**2))*cos(pi*t/T)
        answer += [{'x':t, 'y':y}]
    findMax = []
    for i in range(0, 360):
        findMax += [8*pi**2*cos(2*i/180*pi)*H]
    return answer, 1/30, findMax

def Har_jump():
    answer = []
    for t in range(0, 90):
        answer += [{'x':t, 'y':0}]
    answer += [{'x':90, 'y':-0.4}]
    for t in range(90+1, 180):
        y = ((pi*H)/(2*T))*sin(pi*t/T)*(-1)
        answer += [{'x':t, 'y':y}]
    answer += [{'x':180, 'y':-0.4}]
    for t in range(180+1, 270):
        answer += [{'x':t, 'y':0}]
    answer += [{'x':270, 'y':0.4}]
    for t in range(270+1, 360):
        y = ((pi*H)/(2*T))*sin(pi*t/T)
        answer += [{'x':t, 'y':y}]
    answer += [{'x':360, 'y':0.4}]
    findMax = []
    for i in range(0, 90): findMax += [0]
    for i in range(0, 360):
        findMax += [-32*pi**3*sin(2*i/180*pi)*H]
    return answer, 1, findMax

def Cy_H():
    answer = []
    for t in range(0, 90):
        answer += [{'x':t, 'y':0}]
    for t in range(90, 180):
        y = (-(H/(2*pi))*sin(2*pi*t/T)+(H*t/T))*(-1)+H
        answer += [{'x':t, 'y':y}]
    for t in range(180, 270):
        answer += [{'x':t, 'y':-H}]
    for t in range(270, 360):
        y = (-(H/(2*pi))*sin(2*pi*t/T)+(H*t/T))-4*H
        answer += [{'x':t, 'y':y}]
    findMax = []
    for i in range(0, 91):
        findMax += [-(H/(2*pi))*sin(4*i/180*pi)+(H*i/90)]
    return answer, 60, findMax

def Cy_velocity():
    answer = []
    for t in range(0, 90):
        answer += [{'x':t, 'y':0}]
    for t in range(90, 180):
        y = (H-H*cos(2*pi*t/T))*(-1)
        answer += [{'x':t, 'y':y}]
    for t in range(180, 270):
        answer += [{'x':t, 'y':0}]
    for t in range(270, 360):
        y = (H-H*cos(2*pi*t/T))
        answer += [{'x':t, 'y':y}]
    findMax = []
    for i in range(0, 91):
        findMax += [4*(1-cos(4*i/180*pi))*H]
    return answer, 120, findMax

def Cy_acceleration():
    answer = []
    for t in range(0, 90):
        answer += [{'x':t, 'y':0}]
    for t in range(90, 180):
        y = (H*pi*2*sin(2*pi*t/T))*(-1)
        answer += [{'x':t, 'y':y}]
    for t in range(180, 270):
        answer += [{'x':t, 'y':0}]
    for t in range(270, 360):
        y = (H*pi*2*sin(2*pi*t/T))
        answer += [{'x':t, 'y':y}]
    findMax = []
    for i in range(0, 360):
        findMax += [8*pi**2*sin(4*i/180*pi)*H]
    return answer, 350, findMax

def Cy_jump():
    answer = []
    for t in range(0, 90):
        answer += [{'x':t, 'y':0}]
    for t in range(90, 180):
        y = (H*pi**2*4*cos(2*pi*t/T))*(-1)
        answer += [{'x':t, 'y':y}]
    for t in range(180, 270):
        answer += [{'x':t, 'y':0}]
    for t in range(270, 360):
        y = (H*pi**2*4*cos(2*pi*t/T))
        answer += [{'x':t, 'y':y}]
    findMax = []
    for i in range(0, 360):
        findMax += [256*pi**2*cos(4*i/180*pi)*H]
    return answer, 2200, findMax
