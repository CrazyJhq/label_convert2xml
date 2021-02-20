import os
from write_xml import write_xml,add_object
import cv2

def get_image_size(filename):
    img_temp = cv2.imread(filename)
    img_size = img_temp.shape
    return img_size

f = open("label/label.txt")               # 返回一个文件对象   
line = f.readline()               # 调用文件的 readline()方法   




while line:   
    print(line, end = '')     # 在 Python 3 中使用  
    label = line.split(" ")
    if str(label[5]) != "UAV\n":
        line = f.readline()
        continue
    print(label[4])
    img_size = get_image_size("Imageset/" + str(label[4]))
    if os.path.exists("result/" + str(label[4]).split(".")[0]):     #   如果文件存在，说明该图片中存在多个物体
        add_object(label)
    else:
        write_xml(label,img_size)
#    检测文件是否存在   
#    if os.path.exists("Imageset/" + str(label[4])): 
#        i+=1
    line = f.readline()     
    

f.close()