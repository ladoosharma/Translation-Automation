from xml.dom import NAMESPACE_ERR, minidom
#from XMLDomCreator import XMLDomController
from TranslationXMLGenerator import TranslationXMLGeneratorCntrlr
from FieldTranslationController import FieldTranslationController
from StandardValueSetTranslation import StandardValueSetTranslation
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
trans = TranslationXMLGeneratorCntrlr('D:/Python Projects/Translation-Automation/Python Codes/Translation JSON.txt')
if trans.readFile():
    trans.readDataAndInstantiateObject(trans._content)
    fieldTrans = FieldTranslationController(trans._objectInfoMap, trans._objectPicklistMap)
    standSetTrans = StandardValueSetTranslation(trans._standValueSetMap)
    standSetTrans.generateXML()
    fieldTrans.generateXML()

