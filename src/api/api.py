import os.path
import urllib.request
import gzip
import io
from lxml import etree

from settings import AppSettings

class ApiElement:
    def __init__(self, page, cacheFile, contentType = None):
        self.url = "http://atys.ryzom.com/api/"+page
        self.cacheFile = AppSettings.get().getPath()+"/cache/"+cacheFile
        self.contentType = contentType
        print(self.cacheFile)
        
        if os.path.isfile(self.cacheFile):
            self.data = self.readCache()
        else:
            self.update()
        
    def readCache(self):
        with open(self.cacheFile, "rb")as f:
            self.data = f.read()
            self.decodeData()
            
    def update(self):
        page = urllib.request.urlopen(self.url)
        print(page.geturl())
        print(page.info())
        if self.contentType != None and page.info()["Content-Type"].find(self.contentType) == -1:
            raise ValueError("cannot retrieve element from api : "+page.read().decode("UTF-8"))
        if "Content-Encoding" in page.info() and page.info()["Content-Encoding"] == "gzip":
            zdata = page.read()
            self.data = gzip.decompress(zdata)
        else:
            self.data = page.read()
        self.decodeData()
        
        self.writeCache()
        
    def writeCache(self):
        os.makedirs(os.path.dirname(self.cacheFile), exist_ok=True)
        with open(self.cacheFile, "wb") as f:
            f.write(self.data)
            
    def decodeData(self):
        pass
    
    def checkData(self):
        return True
            
class ApiXmlElement(ApiElement):
    def __init__(self, page, cacheFile):
        super(ApiXmlElement, self).__init__(page, cacheFile)
        
    def decodeData(self):
        self.text = self.data.decode("UTF-8")
        self.tree = etree.parse(io.StringIO(self.text))
        self.root = self.tree.getroot()
        
        if self.root.tag == "error":
            raise ValueError("error : "+self.root.text)
        