
from xml.etree import ElementTree as ET
from Content import Book

class XmlReader:

    def __init__(self, file_path):
        self.path = file_path
        self.root = ET.parse(file_path)
        self.data = None

    def read(self):
        self.data = []
        for b in self.root.findall("book"):
            self.data.append(Book(b.attrib.get("id"), b.find("genre").text, b.find("price").text, b.find("description").text))
        return self.data



# path = "../input/books.xml"
# reader = XmlReader(path)
# books = reader.read()
# print(books)