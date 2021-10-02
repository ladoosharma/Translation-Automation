from xml.dom import minidom

class XMLDomController:

    def __init__(self, fileType) -> None:
        self._root = minidom.Document()
        self._xmlDomParent = self.createDomElement( fileType, 'xmlns', 'http://soap.sforce.com/2006/04/metadata', None)
        self._root.appendChild(self._xmlDomParent)

    def createDomElement(self, rootName, attributeName, attributeValue, text):
        root = None
        if text != None and text != '':
            root = self._root.createElement(rootName)
            content = self._root.createTextNode(text)
            root = self.appendChildToDOM(root, content)
        else:
            root = self._root.createElement(rootName)
        
        if attributeName != None:
            root.setAttribute(attributeName, attributeValue)
        
        return root

    def appendChildToDOM(self, rootElement, childElement):
        rootElement.appendChild(childElement)
        return rootElement
