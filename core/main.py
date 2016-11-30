# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .Ui_main import Ui_MainWindow
from .tabs import Harmonic, Cycloidal

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Harmonic = Harmonic()
        self.Cycloidal = Cycloidal()
        #Harmonic
        self.Har_R.addWidget(self.Harmonic.R)
        self.Har_velocity.addWidget(self.Harmonic.velocity)
        self.Har_acceleration.addWidget(self.Harmonic.acceleration)
        self.Har_jump.addWidget(self.Harmonic.jump)
        #Cycloidal
        self.Cy_R.addWidget(self.Cycloidal.R)
        self.Cy_velocity.addWidget(self.Cycloidal.velocity)
        self.Cy_acceleration.addWidget(self.Cycloidal.acceleration)
        self.Cy_jump.addWidget(self.Cycloidal.jump)
    
    @pyqtSlot(int)
    def on_RarThita_valueChanged(self, value):
        self.Harmonic.R.setAngle(value)
        self.Harmonic.velocity.setAngle(value)
        self.Harmonic.acceleration.setAngle(value)
        self.Harmonic.jump.setAngle(value)
    
    @pyqtSlot(int)
    def on_CyThita_valueChanged(self, value):
        self.Cycloidal.R.setAngle(value)
        self.Cycloidal.velocity.setAngle(value)
        self.Cycloidal.acceleration.setAngle(value)
        self.Cycloidal.jump.setAngle(value)
    
    @pyqtSlot()
    def on_MU_clicked(self):
        self.Harmonic.unitChange(True)
        self.Cycloidal.unitChange(True)
    
    @pyqtSlot()
    def on_IU_clicked(self):
        self.Harmonic.unitChange(False)
        self.Cycloidal.unitChange(False)
