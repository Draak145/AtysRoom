import os.path
from PyQt4 import QtCore

class AppSettings(QtCore.QSettings):
    instance = None
    
    def __init__(self):
        super(AppSettings, self).__init__()
    
    @staticmethod
    def get():
        if AppSettings.instance == None:
            instance = AppSettings()
        return instance
    
    def getPath(self):
        file = self.fileName()
        return os.path.dirname(file)