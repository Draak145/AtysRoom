from api.api import ApiElement
from PyQt4 import QtGui

class ApiImage(ApiElement):
    def __init__(self, page, cacheFile):
        super(ApiImage, self).__init__(page, cacheFile)
        
    def getImage(self):
        return QtGui.QIcon(QtGui.QPixmap(self.cacheFile, "png"))