import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

from gui.guilds.add import AddGuildDialog
from api.guild import ApiGuild
from settings import AppSettings

class GuildsTab(QtGui.QWidget):
    
    def __init__(self):
        super(GuildsTab, self).__init__()
        
        self.vLayout = QtGui.QVBoxLayout(self)
        
        self.hLayout = QtGui.QHBoxLayout()
        self.vLayout.addLayout(self.hLayout)
        
        self.addGuildButton = QtGui.QPushButton("Add")
        self.hLayout.addWidget(self.addGuildButton)
        self.addGuildButton.clicked.connect(self.addGuildPopup)
        
        self.editGuildButton = QtGui.QPushButton("Edit")
        self.hLayout.addWidget(self.editGuildButton)
        
        self.deleteGuildButton = QtGui.QPushButton("Delete")
        self.hLayout.addWidget(self.deleteGuildButton)
        
        self.guildRoomButton = QtGui.QPushButton("Room")
        self.hLayout.addWidget(self.guildRoomButton)
        
        self.hLayout.addStretch(1)
        
        self.guildsTable = QtGui.QTableWidget()
        self.guildsTable.setColumnCount(3)
        
        self.guildsTable.setHorizontalHeaderLabels(["Guild", "Comment", "Key"])
        self.guildsTable.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.guildsTable.horizontalHeader().setMinimumSectionSize(150)
        
        self.guildsTable.verticalHeader().hide()
        self.guildsTable.verticalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        
        self.guildsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.guildsTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.guildsTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.guildsTable.setIconSize(QtCore.QSize(32, 32))
        self.guildsTable.doubleClicked.connect(self.openGuildView)
        
        self.guilds = AppSettings.get().value("guilds", [])
        self.guildClasses = {}
        self.setUpTable()
        
        self.vLayout.addWidget(self.guildsTable)
        
    def openGuildView(self):
        QtGui.QMessageBox.information(self, "data", "pouet %i"%(self.guildsTable.selectedIndexes()[0].row()))
        
        
    def setUpTable(self):
        for key, comment in self.guilds:
            self.addGuild(key, comment)
        
    def addGuildPopup(self):
        key, comment, ok = AddGuildDialog.getGuild(self)
        if ok:
            self.addGuild(key, comment)
            self.guilds.append((key, comment))
            AppSettings.get().setValue("guilds", self.guilds)
            print(AppSettings.get().value("guilds"))
        
    def addGuild(self, key, comment):
        try:
            guild = ApiGuild(key)
            name = guild.getName()
            icon = guild.getIcon()
            self.guildsTable.insertRow(0)
            item = QtGui.QTableWidgetItem(icon, name)
            self.guildsTable.setItem(0, 0, item)
            item = QtGui.QTableWidgetItem(comment)
            self.guildsTable.setItem(0, 1, item)
            item = QtGui.QTableWidgetItem(key)
            self.guildsTable.setItem(0, 2, item)
            
            self.guildClasses[name] = guild
        except:
            QtGui.QMessageBox.information(self, "data", sys.exc_info()[0])
