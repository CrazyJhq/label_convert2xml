# -*- coding:utf-8 -*-


from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree
import xml
from xml.dom import minidom

# generate root node
root = Element('annotation')

eRow = Element("Row")

root.append(eRow)
root.append(eRow)

tree = ElementTree(root)

tree.write("result.xml", encoding = 'utf-8')