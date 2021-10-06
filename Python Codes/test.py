from xml.dom import NAMESPACE_ERR, minidom
#from XMLDomCreator import XMLDomController
from TranslationXMLGenerator import TranslationXMLGeneratorCntrlr
from FieldTranslationController import FieldTranslationController
from StandardValueSetTranslation import StandardValueSetTranslation
from ObjectTranslation import ObjectTranslationController
import os 
  
  
"""root = minidom.Document()
  
xml = root.createElement('root') 
root.appendChild(xml)
  
productChild = root.createElement('product')
productChild.setAttribute('name', 'Geeks for Geeks')
productChild.text = 'testing'
productCode = productChild.createElement('testCode')
productChild.appendChild(productCode)
xml.appendChild(productChild)

xml_str = root.toprettyxml(indent ="\t") 
print(xml_str)

xmlDoc = XMLDomController('root')
child = xmlDoc.createDomElement( 'product', 'name', 'test', None)
xmlDoc.appendChildToDOM(xmlDoc._xmlDomParent, child)
price = xmlDoc.createDomElement('tag', 'test', '123', 'test')
xmlDoc.appendChildToDOM(child, price)
xml_str = xmlDoc._root.toprettyxml(indent ="\t") 
print(xml_str)
"""
#trans = TranslationXMLGeneratorCntrlr('C:/Users/c8916062/Downloads/Case_Task_translation.txt')
trans = TranslationXMLGeneratorCntrlr('Python Codes/Case_Task_translation.txt')
trans._standValuSetTransPath = ''
trans._objectTranslationPath = ''
if trans.readFile():
    trans.readDataAndInstantiateObject(trans._content)
    standSetTrans = StandardValueSetTranslation(trans._standValueSetMap)
    objTran = ObjectTranslationController(trans._validationMap)
    objTran.createObjectXML()
    standSetTrans.generateXML()
    fieldTrans = FieldTranslationController(trans._objectInfoMap, trans._objectPicklistMap, objTran._XMLObjDocMap)
    fieldTrans.generateXML()
    trans.createFileInFolder(standSetTrans._xmlFieldDOMMap, fieldTrans._xmlFieldDOMMap, fieldTrans._objectDomXML)
    trans.createPackageXML()

