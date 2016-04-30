# -*- coding ： utf-8 -*-
# @author tanke
# used in mplcanvas.py

import glob
import numpy as np
from numpy import linalg as LA
import cv2


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
def get_subpix(img, xi, WND_R, DEL_R, BLUR_SIGMA, HESSIAN_SIGMA, GRAY_THR, EIGVAL_THR, CONNECT_R):
    """给定初始点xi，处理图像计算得到亚像素中心点
    @param img 当前的图像，np.array类型
    @param xi  初始中心点
    @param WND_R 亚像素边缘检测窗口半宽
    @param DEL_R 伪边缘点剔除窗口半宽
    @param BLUR_SIGMA 图像高斯平滑因子
    @param HESSIAN_SIGMA Hessian矩阵的高斯求导因子
    @param GRAY_THR 线条灰度大小阈值
    @param EIGVAL_THR 特征值强度阈值
    @param CONNECT_R 亚像素连通搜索半宽
    
    @return xc 亚像素中心点
    """
    p = hessian_points(img, xi, WND_R, DEL_R, BLUR_SIGMA, HESSIAN_SIGMA, GRAY_THR, EIGVAL_THR)
    xv, xh = classify_points(p, CONNECT_R)
    xc = compute_cross_point(xv, xh, WND_R)
    xi = [xc[0] + xi[0] - WND_R, xc[1] + xi[1] - WND_R]
    return xi
    
    
def hessian_points(image, xi, WND_R, DEL_R, BLUR_SIGMA, HESSIAN_SIGMA, GRAY_THR, EIGVAL_THR):
    """提取亚像素线条中心点
    @param * 同get_subpix.param
    
    @return p 亚像素中心点，列表
    """
    #处理区域
    roi = np.double(image[xi[1]-WND_R : xi[1]+WND_R+1, xi[0]-WND_R : xi[0]+WND_R+1])/255.0
    
    #高斯平滑
    blurMask = np.int(2 * np.ceil(3 * BLUR_SIGMA) + 1)
    img = cv2.GaussianBlur(roi, (blurMask,blurMask), BLUR_SIGMA)
    #计算二维高斯核的一阶和二阶微分
    mask = np.int(np.ceil(3 * HESSIAN_SIGMA))
    md = 2*mask +1
    Gx = np.zeros((2*mask+1, 2*mask+1), dtype = np.double)
    Gy = np.zeros((2*mask+1, 2*mask+1), dtype = np.double)
    Gxx = np.zeros((2*mask+1, 2*mask+1), dtype = np.double)
    Gxy = np.zeros((2*mask+1, 2*mask+1), dtype = np.double)
    Gyy = np.zeros((2*mask+1, 2*mask+1), dtype = np.double)
    
    for i in range(-mask, mask+1):
        for j in range(-mask, mask+1):
            Gx[i+mask, j+mask] = -j*np.exp(-0.5*(i**2 + j**2) / HESSIAN_SIGMA**2) / (2*np.pi*HESSIAN_SIGMA**4)
            Gy[i+mask, j+mask] = -i*np.exp(-0.5*(i**2 + j**2) / HESSIAN_SIGMA**2) / (2*np.pi*HESSIAN_SIGMA**4)
            Gxx[i+mask, j+mask] = (j**2 - HESSIAN_SIGMA**2) * np.exp(-0.5*(i**2 + j**2) / HESSIAN_SIGMA**2) / (2*np.pi*HESSIAN_SIGMA**6)
            Gxy[i+mask, j+mask] = i * j * np.exp(-0.5*(i**2 + j**2) / HESSIAN_SIGMA**2) / (2*np.pi*HESSIAN_SIGMA**6)
            Gyy[i+mask, j+mask] = (i**2 - HESSIAN_SIGMA**2) * np.exp(-0.5*(i**2 + j*2) / HESSIAN_SIGMA**2) / (2*np.pi*HESSIAN_SIGMA**6)
    
    #高斯核与图像卷积作为导数
    gx = cv2.filter2D(img, -1, Gx, borderType = cv2.BORDER_CONSTANT)
    gy = cv2.filter2D(img, -1, Gy, borderType = cv2.BORDER_CONSTANT)
    gxx = cv2.filter2D(img, -1, Gxx, borderType = cv2.BORDER_CONSTANT)
    gxy = cv2.filter2D(img, -1, Gxy, borderType = cv2.BORDER_CONSTANT)
    gyy = cv2.filter2D(img, -1, Gyy, borderType = cv2.BORDER_CONSTANT)
    
    #提取亚像素线条中心
    p = []
    DEL_RR = DEL_R**2
    for i in range(2*WND_R+1):
        for j in range(2*WND_R+1):
            if img[i,j] > GRAY_THR and (i-WND_R)**2 + (j-WND_R)**2 > DEL_RR:
                hessian = np.array([[gxx[i,j], gxy[i,j]], [gxy[i,j], gyy[i,j]]])
                w, v= LA.eig(hessian)
                d = max(w)
                vector = v[:, list(w).index(d)]
                #大于阈值，则认为是中心点
                if abs(d) > EIGVAL_THR:
                    nx, ny = vector
                    t = -(nx*gx[i,j] + ny*gy[i,j]) / (nx**2 * gxx[i,j] + 2*nx*ny*gxy[i,j] + ny**2 * gyy[i,j]);
                    nx, ny = t*nx, t*ny
                    if abs(nx) <= 0.5 and abs(ny) <= 0.5:
                        p.append([j + nx, i + ny])
    #返回
    return p
    
    
def classify_points(p, CONNECT_R):
    """分类，两条中心线条
    @param p 未分类的亚像素中心点
    
    @return xv, xh 分类后的两条线段的中心点集
    """
    #连通搜寻
    i = 0
    cp = []
    while i <= 3 and len(p) > 0:
        c = [p.pop(0)];
        flag = 1
        while flag == 1:
            flag = 0
            j = 0
            while j < len(c):
                t = 0
                for k in range(len(p)):
                    if max([abs(round(p[k-t][0] - c[j][0])), abs(round(p[k-t][1] - c[j][1]))]) <= CONNECT_R:
                        flag = 1
                        c.append(p.pop(k-t))
                        t = t + 1
                j = j + 1
        if len(c) >= 10:
            cp.append(c)
            i = i + 1
    #拟合直线计算斜率，并组合为两个数组
    pa = []
    for i in cp:
        c = np.asarray(i)
        k = np.polyfit(c[:,0], c[:,1], 1)
        pa.append(k[0])
    n = 0
    for i in range(1, len(cp)):
        if abs(np.arctan((pa[i] - pa[0]) / (1 + pa[i] * pa[0]))) / np.pi * 180 < 30:
            n = i
            break
    xh = []
    if n > 0:
        xv = np.asarray(cp.pop(0) + cp.pop(n - 1))
        for i in cp:
            xh = xh + i
        xh = np.asarray(xh)
    else:
        xv = np.asarray(cp.pop(0))
        for i in cp:
            xh = xh + i
        xh = np.asarray(xh)
        
    return [xv, xh]
        
    
def compute_cross_point(xv, xh, WND_R):
    """拟合两条线段，并求出交点作为亚像素中心点
    @param xv, xh 两条线条中心点
    
    @return xi 亚像素中心点 
    """
    x0 = [WND_R, WND_R]
    xc = [0,0]
    #抛物线拟合近似椭圆
    v = np.polyfit(xv[:,0], xv[:,1], 2)
    h = np.polyfit(xh[:,0], xh[:,1], 2)
    #解出交点
    a = v[0] - h[0]
    b = v[1] - h[1]
    c = v[2] - h[2]
    delta = b**2 - 4*a*c
    if delta >= 0:
        s = np.sqrt(delta)
        x1 = (-b - s) / (2 * a)
        x2 = (-b + s) / (2 * a)
        distance = lambda x: abs((x-x0[0])) + abs((v[0]*x**2 + v[1]*x + v[2] - x0[1]))
        if distance(x1) < distance(x2):
            xc[0] = x1
            xc[1] = v[0]*x1**2 + v[1]*x1 + v[2]
        else:
            xc[0] = x2
            xc[1] = v[0]*x2**2 + v[1]*x2 + v[2]
    else:
        xc = x0
    return xc