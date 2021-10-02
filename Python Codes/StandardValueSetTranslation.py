from typing import List
from XMLDomCreator import XMLDomController
class StandardValueSetTranslation:

    def __init__(self, valuSetMap:dict) -> None:
        self._valuSetMap = valuSetMap
        self._xmlFieldDOMMap = dict()
        
    def generateXML(self):
        for [eachFld, value] in self._valuSetMap.items():
            XMLValusetDom = XMLDomController('StandardValueSetTranslation')
            XMLValusetDom = self.createPicklistTranslationTag(XMLValusetDom, eachFld, value)
            print(XMLValusetDom._root.toprettyxml(indent ="\t") )
            self._xmlFieldDOMMap[eachFld] = XMLValusetDom

        return self._xmlFieldDOMMap
        
    def generateXMLAndAppendToFolder(self):
        pass

    def createPicklistTranslationTag(self, xmlDoc:XMLDomController , fldName:str, listOfValue:List[object]):
        for eachValue in listOfValue:
            valueTranslation = xmlDoc.createDomElement('valueTranslation',None, None, None)
            masterLabel = xmlDoc.createDomElement('masterLabel', None, None, eachValue["Label"])
            translation = xmlDoc.createDomElement('translation', None, None, eachValue["French Label"])
            xmlDoc.appendChildToDOM(valueTranslation, masterLabel)
            xmlDoc.appendChildToDOM(valueTranslation, translation)
            xmlDoc.appendChildToDOM(xmlDoc._xmlDomParent, valueTranslation)
        return xmlDoc