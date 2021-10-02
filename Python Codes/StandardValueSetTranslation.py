from XMLDomCreator import XMLDomController
class StandardValueSetTranslation:

    def __init__(self, valuSetMap:dict) -> None:
        self._valuSetMap = valuSetMap
        
    def generateXML(self):
        for [eachFld, value] in self._valuSetMap.items():
            XMLValusetDom = XMLDomController('StandardValueSetTranslation')
            XMLValusetDom = self.createPicklistTranslationTag(XMLValusetDom, eachFld)
            print(XMLValusetDom._root.toprettyxml(indent ="\t") )
            self._xmlFieldList.append(XMLValusetDom)

        return self._xmlFieldList
    def generateXMLAndAppendToFolder(self):
        pass

    def createPicklistTranslationTag(self):
        pass