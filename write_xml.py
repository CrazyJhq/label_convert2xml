# -*- coding:utf-8 -*-


from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree
import xml
from xml.dom import minidom

def pretty(e,level=0):
    # 格式化xml文件
    if len(e)>0:
        e.text = "\n"+"\t"*(level+1)
        for child in e:
            pretty(child,level+1)
        child.tail = child.tail[:-1]
    e.tail = "\n"+"\t"*level

def write_xml(label,img_size):
    # generate root node
    root = Element('annotation')

    # generate first child-node head
    folder = SubElement(root, 'folder')
    folder.text = "Imageset"

    # generate first child-node head
    #文件名
    filename1 = SubElement(root, 'filename')
    filename1.text = str(label[4])

    # generate first child-node head
    path = SubElement(root, 'path')
    path.text = "Imageset"

    # generate first child-node head
    source = SubElement(root, 'source')
    database = SubElement(source, 'title')
    database.text = "Unknown"

    # generate first child-node head
    size = SubElement(root, 'size')
    width = SubElement(size, 'width')
    width.text = str(img_size[1])
    height = SubElement(size, 'height')
    height.text = str(img_size[0])
    depth = SubElement(size, 'depth')
    depth.text = str(img_size[2])

    # generate first child-node head
    segmented = SubElement(root, 'segmented')
    segmented.text = "0"

    # generate first child-node head
    # object节点
    object1 = Element("object")
    root.append(object1)
    name = SubElement(object1, 'name')
    name.text = str(label[5]).replace("\n", "")
    pose = SubElement(object1, 'pose')
    pose.text = "Unspecified"
    truncated = SubElement(object1, 'truncated')
    truncated.text = "0"
    difficult = SubElement(object1, 'difficult')
    difficult.text = "0"
    bndbox = SubElement(object1, 'bndbox')
    xmin = SubElement(bndbox, 'xmin')
    xmin.text = str(label[0])
    ymin = SubElement(bndbox, 'ymin')
    ymin.text = str(label[1])
    xmax = SubElement(bndbox, 'xmax')
    xmax.text = str(label[2])
    ymax = SubElement(bndbox, 'ymax')
    ymax.text = str(label[3])

    pretty(root)
    tree = ElementTree(root)
    file_name_0 = str(label[4]).split(".")
    # write out xml data
    tree.write("result/"+str(file_name_0[0])+'.xml', encoding = 'utf-8')

def add_object(label):
    xml_file = xml.etree.ElementTree.parse("result/" + str(label[4]).split(".")[0])
    root = xml_file.getroot()
    object2 = Element("object")
    # generate first child-node head
    # object节点
    root.append(object2)
    name = SubElement(object2, 'name')
    name.text = str(label[5]).replace("\n", "")
    pose = SubElement(object2, 'pose')
    pose.text = "Unspecified"
    truncated = SubElement(object2, 'truncated')
    truncated.text = "0"
    difficult = SubElement(object2, 'difficult')
    difficult.text = "0"
    bndbox = SubElement(object2, 'bndbox')
    xmin = SubElement(bndbox, 'xmin')
    xmin.text = str(label[0])
    ymin = SubElement(bndbox, 'ymin')
    ymin.text = str(label[1])
    xmax = SubElement(bndbox, 'xmax')
    xmax.text = str(label[2])
    ymax = SubElement(bndbox, 'ymax')
    ymax.text = str(label[3])

    pretty(root)
    tree = ElementTree(root)
    file_name_0 = str(label[4]).split(".")
    # write out xml data
    tree.write("result/"+str(file_name_0[0])+'.xml', encoding = 'utf-8')