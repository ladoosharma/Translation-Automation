from XMLDomCreator import XMLDomController
class FieldTranslationController:

    def __init__(self, fieldLabelMap, customPicklistMap, objectDOM:XMLDomController) -> None:#remove last parameter
        self._fieldLabelMap = fieldLabelMap
        self._customPickMap = customPicklistMap
        self._xmlFieldDOMMap = dict()
        self._objectDomXML = objectDOM#remove if doednt work

    def generateXML(self):
        for [eachFld, value] in self._fieldLabelMap.items():
            objName = eachFld.split('.')[0]
            XMLFieldDom = self._objectDomXML[objName]#XMLDomController('CustomFieldTranslation') Remove comment here
            self._fieldParDom = XMLFieldDom.createDomElement('fields', 'xmlns', 'http://soap.sforce.com/2006/04/metadata', None)
            if str(eachFld).endswith('__c'):
                XMLFieldDom = self.createLabelTranslationTag(XMLFieldDom, value['French Label'])
                XMLFieldDom = self.createPicklistTranslationTag(XMLFieldDom, eachFld)
            else:
                XMLFieldDom = self.createCasesAndStartsWithTag(XMLFieldDom, value["French Label Plural"] if "French Label Plural" in value else '', 
                value["French Label"], value["Vowel"] if "Vowel" in value else '')
            XMLFieldDom = self.createGenderTranslationTag(XMLFieldDom, value["Gender"] if "Gender" in value else 'm')

            if "French Help" in value:
                XMLFieldDom = self.createHelpTextTranslationTag(XMLFieldDom, value['French Help'])

            XMLFieldDom = self.createNameTag(XMLFieldDom, eachFld.split('.')[1])
            XMLFieldDom.appendChildToDOM(XMLFieldDom._xmlDomParent, self._fieldParDom)
            print(XMLFieldDom._root.toprettyxml(indent ="\t") )
            self._objectDomXML[objName] =XMLFieldDom 
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
                #xmlDomObject.appendChildToDOM(xmlDomObject._xmlDomParent, picklistValuesTag)
                xmlDomObject.appendChildToDOM(self._fieldParDom, picklistValuesTag)

            return xmlDomObject    
            #print(xmlDomObject._root.toprettyxml(indent ="\t") )
            

        return xmlDomObject

    def createHelpTextTranslationTag(self, xmlDomObject:XMLDomController, translatedText:str):
        help = xmlDomObject.createDomElement( 'label', None, None, translatedText)
        #xmlDomObject.appendChildToDOM(xmlDomObject._xmlDomParent, help)
        xmlDomObject.appendChildToDOM(self._fieldParDom, help)
        return xmlDomObject

    def createNameTag(self, xmlDomObject, apiName):
        name = xmlDomObject.createDomElement( 'name', None, None, apiName)
        #xmlDomObject.appendChildToDOM(xmlDomObject._xmlDomParent, name)
        xmlDomObject.appendChildToDOM(self._fieldParDom, name)
        return xmlDomObject

    def createGenderTranslationTag(self, xmlDomObject, genderName):
        genderName = 'Masculine' if genderName == 'm' else 'Feminine'
        gender = xmlDomObject.createDomElement( 'gender', None, None, genderName)
        #xmlDomObject.appendChildToDOM(xmlDomObject._xmlDomParent, gender)
        xmlDomObject.appendChildToDOM(self._fieldParDom, gender)
        return xmlDomObject
    def createLabelTranslationTag(self, xmlDomObject, translatedLabel):
        label = xmlDomObject.createDomElement( 'label', None, None, translatedLabel)
        #xmlDomObject.appendChildToDOM(xmlDomObject._xmlDomParent, label)
        xmlDomObject.appendChildToDOM(self._fieldParDom, label)
        return xmlDomObject
    
    def createCasesAndStartsWithTag(self, xmlDomObject:XMLDomController, pluralLabel:str, singularLabel:str, isVowel:str):
        if pluralLabel != None and pluralLabel != '':
            caseValPlural = xmlDomObject.createDomElement('caseValues', None, None, None)
            pluralTag = xmlDomObject.createDomElement('plural', None, None, 'true')
            pluralValueTag = xmlDomObject.createDomElement('value', None, None, pluralLabel)
            xmlDomObject.appendChildToDOM(caseValPlural, pluralTag)
            xmlDomObject.appendChildToDOM(caseValPlural, pluralValueTag)
            xmlDomObject.appendChildToDOM(self._fieldParDom, caseValPlural)
        if singularLabel != None and singularLabel != '':
            caseValSingular = xmlDomObject.createDomElement('caseValues', None, None, None)
            singularTag = xmlDomObject.createDomElement('plural', None, None, 'false')
            singularValueTag = xmlDomObject.createDomElement('value', None, None, singularLabel)
            startsWithSingular = xmlDomObject.createDomElement('startsWith', None, None, "Vowel" if (isVowel == 'true' and isVowel != '')  else "Consonant")
            xmlDomObject.appendChildToDOM(caseValSingular, singularTag)
            xmlDomObject.appendChildToDOM(caseValSingular, singularValueTag)
            xmlDomObject.appendChildToDOM(self._fieldParDom, caseValSingular)
        
        startsWith = xmlDomObject.createDomElement('startsWith', None, None, "Vowel" if (isVowel == 'true' and isVowel != '')  else "Consonant")
        xmlDomObject.appendChildToDOM(self._fieldParDom, startsWith)
        return xmlDomObject