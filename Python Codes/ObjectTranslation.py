from XMLDomCreator import XMLDomController

class ObjectTranslationController:

    def __init__(self, validationMap:dict) -> None:
        """Constructor of the class

        Args:
            validationMap (dict): this will hold the map of validation object , Key will be object API Name
        """
        self._validationMap = validationMap
        self._XMLObjDocMap = dict()
        

    def createObjectXML(self):
        """This method will gnerate the XML Object for each object in CSV
        """
        if self._validationMap != None:
            for [key, val] in self._validationMap.items():
                objTag = XMLDomController('CustomObjectTranslation')
                caseValueP = objTag.createDomElement('caseValues', None, None, None)
                caseValuePbool = objTag.createDomElement('plural', None, None, 'true')
                caseValuePVal = objTag.createDomElement('value', None, None, '')
                caseValueS = objTag.createDomElement('caseValues', None, None, None)
                caseValueSbool = objTag.createDomElement('plural', None, None, 'false')
                caseValueSVal = objTag.createDomElement('value', None, None, '')
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
        """This method will create the validation XML message which will be appended to the parent object XML

        Args:
            objXMLDom (XMLDomController):DOM Object of parent
            listOfValidation (list): List of validation message object

        Returns:
            XMLDomController: this will return the parent DOM object
        """
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
        """This method will generate XML for gender of object and attach to oarent object XML

        Args:
            xmlDom (XMLDomController, optional): This is the parent DOM object of Object XML. Defaults to None.
            gender (str, optional): Object Gender. Defaults to 'Masculine'.

        Returns:
            XMLDomController: this will return the parent DOM object
        """
        genderTag = xmlDom.createDomElement('gender', None, None, gender)
        xmlDom.appendChildToDOM(xmlDom._xmlDomParent, genderTag)
        return xmlDom

    def createStartsWithXML(self,xmlDom:XMLDomController=None, startsWith:str='Vowel'):
        """This method will generate XML for starts with tag

        Args:
            xmlDom (XMLDomController, optional): This is the parent DOM object of Object XML. Defaults to None.
            startsWith (str, optional): Object Gender. Defaults to 'Vowel'.

        Returns:
            XMLDomController: this will return the parent DOM object
        """
        startsTag = xmlDom.createDomElement('startsWith', None, None, startsWith)
        xmlDom.appendChildToDOM(xmlDom._xmlDomParent, startsTag)
        return xmlDom


                