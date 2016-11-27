# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class chart(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setParent(parent)
        self.thita = 360
        self.path = []
        self.color = Qt.black
        self.rate = 1
        self.maxima = [0]
    
    def setAngle(self, thita):
        self.thita = thita
        self.update()
    def setPath(self, path):
        self.path = path
        self.update()
    def setColor(self, color):
        self.color = color
        self.update()
    def setRate(self, rate):
        self.rate = rate
        self.update()
    def setMaxima(self, findMax):
        self.maxima = findMax
    def setFormula(self, formula):
        self.setToolTip(formula)
    
    def findMax(self):
        maxima = max(self.maxima)
        return maxima, self.maxima.index(maxima)
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(), QBrush(Qt.white))
        painter.translate(0, self.height()/2)
        pen = QPen()
        pen.setColor(Qt.black)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawLine(QPointF(0, 0), QPointF(self.width()*2, 0))
        pen.setColor(Qt.red)
        painter.setPen(pen)
        painter.drawLine(QPointF(self.width()*1/4, self.height()*2), QPointF(self.width()*1/4, self.height()*2*(-1)))
        painter.drawLine(QPointF(self.width()*2/4, self.height()*2), QPointF(self.width()*2/4, self.height()*2*(-1)))
        painter.drawLine(QPointF(self.width()*3/4, self.height()*2), QPointF(self.width()*3/4, self.height()*2*(-1)))
        painter.drawText(QPointF(self.width()*1/4, self.height()/2), 'π/4')
        painter.drawText(QPointF(self.width()*2/4, self.height()/2), 'π/2')
        painter.drawText(QPointF(self.width()*3/4, self.height()/2), '3π/4')
        #Graph
        painterpath = QPainterPath()
        for e in self.path[0:self.thita]:
            painterpath.lineTo(QPointF(e['x']/360*self.width(), e['y']/self.rate*self.height()))
        pen.setColor(self.color)
        pen.setWidth(4)
        painter.setPen(pen)
        painter.drawPath(painterpath)
        nowMax = self.maxima[0:self.thita-90]
        if nowMax and self.thita >= 90:
            maxima = max(nowMax)
            pen.setColor(Qt.black)
            pen.setWidth(1)
            painter.setPen(pen)
            pos = self.width()*(nowMax.index(maxima)+90)/360
            painter.drawLine(QPointF(pos, self.height()*2), QPointF(pos, self.height()*2*(-1)))
            painter.drawText(QPointF(pos, -self.height()/2+25), str(maxima)[0:8])
