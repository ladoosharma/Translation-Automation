import json
from os import error
from typing import List
from XMLDomCreator import XMLDomController

class TranslationXMLGeneratorCntrlr:
    #this will be changed
    _standValuSetTransPath = 'C:/Users/c8916062/OneDrive - Lowe\'s Companies Inc/Documents/TranslationAutomation/Translation_SFDC/force-app/main/default/standardValueSetTranslations'
    # this will be changed
    _objectTranslationPath = 'C:/Users/c8916062/OneDrive - Lowe\'s Companies Inc/Documents/TranslationAutomation/Translation_SFDC/force-app/main/default/objectTranslations'

    def __init__(self, filePath) -> None:
        self._filePath = filePath
        self._objectInfoMap = dict()
        self._objectPicklistMap = dict()
        self._standValueSetMap = dict()
        self._validationMap = dict()
        self._content = None

    def readDataAndInstantiateObject(self, content):
        for [key, val] in content.items():
           
            if str(key).startswith('O.'):
                objName = key.split('-')[0]
                objName = objName.replace('O.','')
                self._validationMap[objName] = list()
                for eachFld in val:
                    if 'Field Name' in eachFld:
                        self._objectInfoMap[objName+'.'+ eachFld['Field Name']] = eachFld
                        if 'P.'+objName+'-'+eachFld['Field Name'] in content:
                            self._objectPicklistMap[objName+'.'+ eachFld['Field Name']] = content['P.'+objName+'-'+eachFld['Field Name']]
                        elif 'S.'+objName +'-'+ eachFld['Field Name'] in content:
                            self._standValueSetMap[eachFld['Field Name']] = content['S.'+objName+'-'+eachFld['Field Name']]
                        
            elif str(key).startswith('V.'):
                objName = objName.replace('V.','')
                self._validationMap[objName] = val
                
            elif str(key).startswith('S.'):
                gFldName = key.split('-')[1]
                self._standValueSetMap[gFldName] = val

    def readFile(self):
        try:
            with open(self._filePath, 'rb') as fin:
                self._content = json.load(fin)
                #self.readDataAndInstantiateObject(content)
                print(self._objectInfoMap)
                return True
        except:
            raise error
            return False
    
    def createFileInFolder(self, valusetDocMap:dict, fieldTransDocMap: dict, objTranslationDocMap: dict):
        '''for [fileName , fileContent] in fieldTransDocMap.items():
            objName = str(fileName.split('.')[0]).strip()
            fldName = str(fileName.split('.')[1]).strip()
            
            with open(self._objectTranslationPath+'/'+objName+'-fr/'+fldName+'.fieldTranslation-meta.xml', "wb") as f:
                f.write(fileContent._root.toprettyxml(indent ="\t", encoding="utf-8")) 
        '''
        for [fileName , fileContent] in valusetDocMap.items():
            with open(self._standValuSetTransPath+'/'+fileName+'-fr'+'.standardValueSetTranslation-meta.xml', "wb") as f:
                f.write(fileContent._root.toprettyxml(indent ="\t", encoding="utf-8")) 
        for [fileName , fileContent] in objTranslationDocMap.items():
            with open(self._objectTranslationPath+'/'+fileName+'-fr'+'/'+fileName+'-fr'+'.objectTranslation-meta.xml', "wb") as f:
                f.write(fileContent._root.toprettyxml(indent ="\t", encoding="utf-8")) 

    def createPackageXML(self):
        package = XMLDomController('Package')
        stdTranslationMember = package.createDomElement('types', None, None, None)
        nameStdTranTag = package.createDomElement('name',None, None, 'StandardValueSetTranslation')
        fieldMember = package.createDomElement('types', None, None, None)
        nameFieldTag = package.createDomElement('name',None, None, 'CustomField')
        package.appendChildToDOM(package._xmlDomParent, stdTranslationMember)
        package.appendChildToDOM(package._xmlDomParent, fieldMember)
        for [fieldApiName, val] in self._objectInfoMap.items():
            memberFld = package.createDomElement('members',None, None, fieldApiName)
            package.appendChildToDOM(fieldMember, memberFld)
        
        for [fieldApiName, val] in self._standValueSetMap.items():
            memberFld = package.createDomElement('members',None, None, fieldApiName)
            package.appendChildToDOM(stdTranslationMember, memberFld)
        
        package.appendChildToDOM(fieldMember, nameFieldTag)
        package.appendChildToDOM(stdTranslationMember, nameStdTranTag)
        with open('C:/Users/c8916062/OneDrive - Lowe\'s Companies Inc\Documents/TranslationAutomation/Translation_SFDC/manifest/package.xml', "wb") as f:
                f.write(package._root.toprettyxml(indent ="\t", encoding="utf-8"))    


   


    