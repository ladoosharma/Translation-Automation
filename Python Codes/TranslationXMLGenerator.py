import json
from os import error
from typing import List
from XMLDomCreator import XMLDomController

class TranslationXMLGeneratorCntrlr:
    # path of the standard value set folder 
    _standValuSetTransPath = ''
    # path of the objectTranslation folder 
    _objectTranslationPath = ''

    def __init__(self, filePath:str) -> None:
        """Constructo of the class

        Args:
            filePath (str): path of JSON file which is extracted from the .xlsx file
        """
        self._filePath = filePath
        self._objectInfoMap = dict()
        self._objectPicklistMap = dict()
        self._standValueSetMap = dict()
        self._validationMap = dict()
        self._content = None

    def readDataAndInstantiateObject(self, content:dict):
        """This method will read the file and create the map of object, field and picklist data

        Args:
            content (dict): map of excel tabs and its data 
        """
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
        """This method reads the JSON file 

        Raises:
            error: [description]

        Returns:
            Boolean : return true if file is processed successfully
        """
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
        """[summary]

        Args:
            valusetDocMap (dict): picklist map of value set
            fieldTransDocMap (dict): field information map
            objTranslationDocMap (dict): object inormation map
        """
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

    def createPackageXML(self, fileLocation:str):
        """this method will create package xml files based on the XML generated from the respective classes

        Args:
            fileLocation (str): location of manifest folder where package needs to be created
        """
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
        with open(fileLocation, "wb") as f:
                f.write(package._root.toprettyxml(indent ="\t", encoding="utf-8"))    


   


    