import json
from os import error
from XMLDomCreator import XMLDomController

class TranslationXMLGeneratorCntrlr:
    #this will be changed
    _standValuSetTransPath = 'D:/Python Projects/Translation-Automation/force-app/main/default/standardValueSetTranslations'
    # this will be changed
    _objectTranslationPath = 'D:/Python Projects/Translation-Automation/force-app/main/default/objectTranslations'

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
                
                for eachFld in val:
                    if 'Field Name' in eachFld:
                        self._objectInfoMap[objName+'.'+ eachFld['Field Name']] = eachFld
                        if 'P.'+objName+'-'+eachFld['Field Name'] in content:
                            self._objectPicklistMap[objName+'.'+ eachFld['Field Name']] = content['P.'+objName+'-'+eachFld['Field Name']]
                        elif 'S.'+objName +'-'+ eachFld['Field Name'] in content:
                            self._standValueSetMap[eachFld['Field Name']] = content['S.'+objName+'-'+eachFld['Field Name']]
                        elif 'V.'+objName +'-'+ eachFld['Field Name'] in content:
                            pass
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
            print(error)
            return False
    
    def createFileInFolder(self, valusetDocMap:dict, fieldTransDocMap: dict):
        for [fileName , fileContent] in fieldTransDocMap.items():
            objName = str(fileName.split('.')[0]).strip()
            fldName = str(fileName.split('.')[1]).strip()
            
            with open(self._objectTranslationPath+'/'+objName+'-fr/'+fldName+'.fieldTranslation-meta.xml', "w", encoding="utf-8") as f:
                f.write(fileContent._root.toprettyxml(indent ="\t")) 

        for [fileName , fileContent] in valusetDocMap.items():
            with open(self._standValuSetTransPath+'/'+fileName+'-fr'+'.standardValueSetTranslation-meta.xml', "w", encoding="utf-8") as f:
                f.write(fileContent._root.toprettyxml(indent ="\t")) 

    def createPackageXML(self):
        package = XMLDomController('Package')
        stdTranslationMember = package.createDomElement('types', None, None, None)
        nameStdTranTag = package.createDomElement('name',None, None, 'StandardValueSetTranslation')
        package.appendChildToDOM(stdTranslationMember, nameStdTranTag)
        fieldMember = package.createDomElement('types', None, None, None)
        nameFieldTag = package.createDomElement('name',None, None, 'CustomField')
        package.appendChildToDOM(fieldMember, nameFieldTag)
        package.appendChildToDOM(package._xmlDomParent, stdTranslationMember)
        package.appendChildToDOM(package._xmlDomParent, fieldMember)
        for [fieldApiName, val] in self._objectInfoMap.items():
            memberFld = package.createDomElement('members',None, None, fieldApiName)
            package.appendChildToDOM(fieldMember, memberFld)

        print(package._root.toprettyxml())    


   


    