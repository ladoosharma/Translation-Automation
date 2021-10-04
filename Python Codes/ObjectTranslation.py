from XMLDomCreator import XMLDomController

class ObjectTranslationController:

    def __init__(self, validationMap:dict) -> None:
        self._validationMap = validationMap
        self._XMLObjDocMap = dict()
        

    def createObjectXML(self):
        if self._validationMap != None:
            for [key, val] in self._validationMap.items():
                objTag = XMLDomController('CustomObjectTranslation')
                caseValueP = objTag.createDomElement('caseValues', None, None, None)
                caseValuePbool = objTag.createDomElement('plural', None, None, 'true')
                caseValuePVal = objTag.createDomElement('value', None, None, 'CHANGE_VALUE_HERE_OR_DELETE')
                caseValueS = objTag.createDomElement('caseValues', None, None, None)
                caseValueSbool = objTag.createDomElement('plural', None, None, 'false')
                caseValueSVal = objTag.createDomElement('value', None, None, 'CHANGE_VALUE_HERE_OR_DELETE')
                objTag.appendChildToDOM(caseValueP, caseValuePbool)
                objTag.appendChildToDOM(caseValueP, caseValuePVal)
                objTag.appendChildToDOM(objTag._xmlDomParent, caseValueP)
                objTag.appendChildToDOM(caseValueS, caseValueSbool)
                objTag.appendChildToDOM(caseValueS, caseValueSVal)
                objTag.appendChildToDOM(objTag._xmlDomParent, caseValueS)
                objTag = self.createGenderXML(objTag)
                objTag = self.createStartsWithXML(objTag)
                objTag = self.addValidationTagForObj(objTag, val)
                self._XMLObjDocMap[key] = objTag

    def addValidationTagForObj(self, objXMLDom:XMLDomController, listOfValidation:list):
        if listOfValidation != None:
            for eachValidation in listOfValidation:
                validationTag = objXMLDom.createDomElement('validationRules', None, None, None)
                nameTag = objXMLDom.createDomElement('name', None, None, eachValidation["Rule Name"])
                messageTag = objXMLDom.createDomElement('errorMessage', None, None, eachValidation["Error Message"])
                objXMLDom.appendChildToDOM(validationTag, messageTag)
                objXMLDom.appendChildToDOM(validationTag, nameTag)
                objXMLDom.appendChildToDOM(objXMLDom._xmlDomParent, validationTag)
            
        
        return objXMLDom

    def createGenderXML(self,xmlDom:XMLDomController=None, gender:str='Masculine'):
        genderTag = xmlDom.createDomElement('gender', None, None, gender)
        xmlDom.appendChildToDOM(xmlDom._xmlDomParent, genderTag)
        return xmlDom

    def createStartsWithXML(self,xmlDom:XMLDomController=None, startsWith:str='Vowel'):
        startsTag = xmlDom.createDomElement('startsWith', None, None, startsWith)
        xmlDom.appendChildToDOM(xmlDom._xmlDomParent, startsTag)
        return xmlDom


                