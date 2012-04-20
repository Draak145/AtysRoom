from PyQt4 import QtGui

class AddGuildDialog(QtGui.QDialog):
    def __init__(self, parent):
        super(AddGuildDialog, self).__init__(parent)
        
        self.guildKey = ""
        self.guildComment = ""
        
        self.vLayout = QtGui.QVBoxLayout(self)
        
        self.grid = QtGui.QGridLayout()
        
        self.guildKeyLabel = QtGui.QLabel("Guild Key :")
        self.grid.addWidget(self.guildKeyLabel, 0, 0)
        
        self.guildKeyEdit = QtGui.QLineEdit()
        self.grid.addWidget(self.guildKeyEdit, 0, 1)
        
        self.commentLabel = QtGui.QLabel("Comment :")
        self.grid.addWidget(self.commentLabel, 1, 0)
        
        self.commentEdit = QtGui.QLineEdit()
        self.grid.addWidget(self.commentEdit, 1, 1)
        
        self.vLayout.addLayout(self.grid)
        
        self.actionLayout = QtGui.QHBoxLayout()
        self.actionLayout.addStretch(1)
        
        self.cancelButton = QtGui.QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.rejected)
        self.actionLayout.addWidget(self.cancelButton)
        
        self.acceptButton = QtGui.QPushButton("OK")
        self.acceptButton.clicked.connect(self.accepted)
        self.actionLayout.addWidget(self.acceptButton)
        
        self.vLayout.addLayout(self.actionLayout)
        
        self.setMinimumWidth(300)
        
    def accepted(self):
        self.guildKey = self.guildKeyEdit.text()
        self.guildComment = self.commentEdit.text()
        self.ok = True
        self.close()
        
    def rejected(self):
        self.ok = False
        self.close()
        
    @staticmethod
    def getGuild(parent):
        dialog = AddGuildDialog(parent)
        dialog.exec_()
        return (dialog.guildKey, dialog.guildComment, dialog.ok)
    