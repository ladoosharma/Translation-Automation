from XMLDomCreator import XMLDomController
class FieldTranslationController:

    def __init__(self, fieldLabelMap, customPicklistMap) -> None:
        self._fieldLabelMap = fieldLabelMap
        self._customPickMap = customPicklistMap
        self._xmlFieldDOMMap = dict()

    def generateXML(self):
        for [eachFld, value] in self._fieldLabelMap.items():
            XMLFieldDom = XMLDomController('CustomFieldTranslation')
            XMLFieldDom = self.createLabelTranslationTag(XMLFieldDom, value['French Label'])
            #XMLFieldDom = self.createHelpTextTranslationTag(XMLFieldDom, value['French Help'])
            XMLFieldDom = self.createPicklistTranslationTag(XMLFieldDom, eachFld)
            XMLFieldDom = self.createGenderTranslationTag(XMLFieldDom, 'Masculine')
            XMLFieldDom = self.createNameTag(XMLFieldDom, eachFld.split('.')[1])
            print(XMLFieldDom._root.toprettyxml(indent ="\t") )
            self._xmlFieldDOMMap[eachFld] = XMLFieldDom

        return self._xmlFieldDOMMap

    def createPicklistTranslationTag(self, xmlDomObject:XMLDomController, fieldApiName:str):
        if fieldApiName in self._customPickMap:
            for eachPicklist in self._customPickMap[fieldApiName]:
                picklistValuesTag = xmlDomObject.createDomElement( 'picklistValues', None, None, None)
                masterLabelTag = xmlDomObject.createDomElement( 'masterLabel', None, None, eachPicklist['Label'])
                translationTag = xmlDomObject.createDomElement( 'translation', None, None, eachPicklist['French'])
                xmlDomObject.appendChildToDOM(picklistValuesTag, masterLabelTag)
                xmlDomObject.appendChildToDOM(picklistValuesTag, translationTag)
                xmlDomObject.appendChildToDOM(xmlDomObject._xmlDomParent, picklistValuesTag)

            return xmlDomObject    
            #print(xmlDomObject._root.toprettyxml(indent ="\t") )
            

        return xmlDomObject

    def createHelpTextTranslationTag(self, xmlDomObject:XMLDomController, translatedText:str):
        help = xmlDomObject.createDomElement( 'label', None, None, translatedText)
        xmlDomObject.appendChildToDOM(xmlDomObject._xmlDomParent, help)
        return xmlDomObject

    def createValidationTranslationTag(self, xmlDomObject):
        return xmlDomObject

    def createNameTag(self, xmlDomObject, apiName):
        name = xmlDomObject.createDomElement( 'name', None, None, apiName)
        xmlDomObject.appendChildToDOM(xmlDomObject._xmlDomParent, name)
        return xmlDomObject

    def createGenderTranslationTag(self, xmlDomObject, genderName):
        gender = xmlDomObject.createDomElement( 'gender', None, None, genderName)
        xmlDomObject.appendChildToDOM(xmlDomObject._xmlDomParent, gender)
        return xmlDomObject
    def createLabelTranslationTag(self, xmlDomObject, translatedLabel):
        label = xmlDomObject.createDomElement( 'label', None, None, translatedLabel)
        xmlDomObject.appendChildToDOM(xmlDomObject._xmlDomParent, label)
        return xmlDomObject