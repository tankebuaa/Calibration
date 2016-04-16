'''
Created on 2016年3月26日

@author: tanke

This script alets the user enter the name of the images (base name, numbering scheme,...
'''
# coding = utf-8

import glob
def data_calib():
    # 获取图像文件名类型
    fileType = dict({1:"ras", 2:"bmp", 3:"tif", 4:"pgm", 5:"ppm", 6:"jpg", 7:"jpeg", 8:"png"})
    typeId = None;
    while typeId == None:
        try:
            typeId = int(input("Please enter image type(1: ras, 2: bmp, 3: tif, 4: pgm, 5: ppm, 6: jpg, 7: jpeg, 8：png):"))
            typeId = fileType[typeId]
        except (ValueError, KeyError):
            print("Please input a number[1-8]:")
            typeId = None
    # 获取文件名的基本名
    baseName = None
    class BasenameErr(Exception):pass# 产生文件名异常
    while baseName == None:
        try:
            baseName = str(input("Plesae Input the basename:"))
            f = glob.glob("../*/" + baseName + "*." +typeId)
            if len(f) == 0:
                raise BasenameErr()
        except BasenameErr:
            print("baseName Error!")
            baseName = None
    print(">>>>>> Image files:{}".format(f))
    return f