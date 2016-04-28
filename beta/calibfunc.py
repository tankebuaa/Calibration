# -*- coding ： utf-8 -*-
# @author tanke
# used in mplcanvas.py

import glob
import numpy as np



# --------------------------------------------------------MplData.picName--------------------------------------------------------
def get_file_name():
    """读取当前目录的图片
    @return f 文件名字符串列表
    """
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
    
    
# --------------------------------------------------------MplData.point-----------------------------------------------------------
def get_subpix(img, xi, WND_R, DEL_R, HESSIAN_SIGMA, CONNECT_R, GRAY_THR, EIGVAL_THR):
    """给定初始点xi，处理图像计算得到亚像素中心点
    @param img 当前的图像，np.array类型
    @param xi  初始中心点
    @param WND_R 亚像素边缘检测窗口半宽
    @param DEL_R 伪边缘点剔除窗口半宽
    @param HESSIAN_SIGMA Hessian矩阵的高斯求导因子
    @param CONNECT_R 亚像素连通搜索半宽
    @param GRAY_THR 线条灰度大小阈值
    @param EIGVAL_THR 特征值强度阈值
    @return xc 亚像素中心点
    """
    p = hessian_points(img, xi, WND_R, DEL_R, HESSIAN_SIGMA, GRAY_THR, EIGVAL_THR)
    xv, xh = classify_points(p, CONNECT_R)
    xc = compute_cross(xi, xv, xh)
    
    
def hessian_points(img, xi, WND_R, DEL_R, HESSIAN_SIGMA, GRAY_THR, EIGVAL_THR):
    """提取亚像素线条中心点
    @param . 同get_subpix.param
    @return p 亚像素中心点，np.array(N*2)
    """
    
    
def classify_points(p, CONNECT_R):
    """分类，两条中心线条
    @param p 未分类的亚像素中心点
    @return xv, xh 分类后的两条线段的中心点集
    """
    
    
def compute_cross(xi, xv, xh):
    """拟合两条线段，并求出交点作为亚像素中心点
    @param xv, xh 两条线条中心点
    @return xi 亚像素中心点 
    """