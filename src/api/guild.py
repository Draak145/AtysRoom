from api.api import ApiXmlElement

from settings import AppSettings
from api.image import ApiImage

class ApiGuildIcon(ApiImage):
    def __init__(self, key):
        self.key = key
        self.page = "guild_icon.php?icon=%s&size=%s"%(key, "b")
        self.cacheName = "images/guilds/%s"%(key)
        
        super(ApiGuildIcon, self).__init__(self.page, self.cacheName)


class ApiGuild(ApiXmlElement):
    def __init__(self, key):
        self.key = key
        self.page = "guild.php?key=%s"%(key)
        self.cacheName = "guilds/%s"%(key)
        
        super(ApiGuild, self).__init__(self.page, self.cacheName)
            
    def getName(self):
        for node in self.root.iter("name"):
            return node.text
        
    def getIcon(self):
        for node in self.root.iter("icon"):
            self.icon = ApiGuildIcon(node.text)
            return self.icon.getImage()