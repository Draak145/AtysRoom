#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

from gui.guilds.tab import GuildsTab
from settings import AppSettings

class MainWindow(QtGui.QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('AtysRoom')
        
        self.horizontalLayout = QtGui.QHBoxLayout(self)
        self.horizontalLayout.setMargin(0)
        
        tabs = QtGui.QTabWidget(self)
        tabs.addTab(GuildsTab(), "Guilds")
        
        self.horizontalLayout.addWidget(tabs)
    
        self.show()

def main():    
    app = QtGui.QApplication(sys.argv)
    QtCore.QCoreApplication.setOrganizationName("atysRoom")
    QtCore.QCoreApplication.setApplicationName("atysRoom")
    AppSettings.get()
    w = MainWindow()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
