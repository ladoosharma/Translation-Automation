from typing import List
from XMLDomCreator import XMLDomController
class StandardValueSetTranslation:

    def __init__(self, valuSetMap:dict) -> None:
        """Constructor for the class

        Args:
            valuSetMap (dict): standard picklist value map
        """
        self._valuSetMap = valuSetMap
        self._xmlFieldDOMMap = dict()
        
    def generateXML(self):
        """This method will generate the picklist XML for value set

        Returns:
            XMLDomController: retrun parent dom
        """
        for [eachFld, value] in self._valuSetMap.items():
            XMLValusetDom = XMLDomController('StandardValueSetTranslation')
            XMLValusetDom = self.createPicklistTranslationTag(XMLValusetDom, eachFld, value)
            print(XMLValusetDom._root.toprettyxml(indent ="\t") )
            self._xmlFieldDOMMap[eachFld] = XMLValusetDom
        return self._xmlFieldDOMMap
        
    def generateXMLAndAppendToFolder(self):
        pass

    def createPicklistTranslationTag(self, xmlDoc:XMLDomController , fldName:str, listOfValue:List[object]):
        """This method will create pilist tag and attach to the standardValuSet XML

        Args:
            xmlDoc (XMLDomController): standardValuSet XML Object
            fldName (str): API Name of standardValuSet
            listOfValue (List[object]): List of value set options

        Returns:
            XMLDomController: retrun parent dom
        """
        for eachValue in listOfValue:
            valueTranslation = xmlDoc.createDomElement('valueTranslation',None, None, None)
            masterLabel = xmlDoc.createDomElement('masterLabel', None, None, eachValue["Label"])
            translation = xmlDoc.createDomElement('translation', None, None, eachValue["French Label"])
            xmlDoc.appendChildToDOM(valueTranslation, masterLabel)
            xmlDoc.appendChildToDOM(valueTranslation, translation)
            xmlDoc.appendChildToDOM(xmlDoc._xmlDomParent, valueTranslation)
        return xmlDoc
    