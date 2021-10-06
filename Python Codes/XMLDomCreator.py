from os import path
from xml.dom import minidom
import xml.etree.ElementTree as eTree

class XMLDomController:

    def __init__(self, fileType:str) -> None:
        """Constructor for the class

        Args:
            fileType (str): type of the parent XML dom name
        """
        self._root = minidom.Document()
        if fileType != None:
            self._xmlDomParent = self.createDomElement( fileType, 'xmlns', 'http://soap.sforce.com/2006/04/metadata', None)
            self._root.appendChild(self._xmlDomParent)
            self._existingParsedDoc = None

    def createDomElement(self, rootName:str, attributeName:str, attributeValue:str, text:str):
        """This method will create new nodes

        Args:
            rootName (str): root XML dom
            attributeName (str): attribute name for new XML
            attributeValue (str): attribute value name for new XML
            text (str): inner text for new XML

        Returns:
            XMLDomController: root dom object
        """
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

    def appendChildToDOM(self, rootElement:minidom.Document, childElement):
        """this method will apend dom element to parent

        Args:
            rootElement (minidom.Document): parent elemnent
            childElement ([type]): child element

        Returns:
            XMLDomController: root dom object
        """
        rootElement.appendChild(childElement)
        return rootElement


