import json
from os import error
class TranslationXMLGeneratorCntrlr:
    #this will be changed
    _standValuSetTransPath = 'C:/Usersc8916062OneDrive - Lowe\'s Companies Inc/Documents/TranslationAutomation/Translation_SFDC/force-app/main/default/standardValueSetTranslations'
    # this will be changed
    _objectTranslAtionPath = 'C:/Users/c8916062/OneDrive - Lowe\'s Companies Inc/Documents/TranslationAutomation/Translation_SFDC/force-app/main/default/objectTranslations/Account-fr'

    """_objectInfoMap = dict()
    _objectPicklistMap = dict()
    _standValueSetMap = dict()
    _validationMap = dict()"""

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
        


    