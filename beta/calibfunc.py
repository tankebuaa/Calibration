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
    xi = [xc[0] + xi[0] - 2*WND_R, xc[1] +xi[1] - 2*WND_R]
    return xi
    
    
def hessian_points(image, xi, WND_R, DEL_R, BLUR_SIGMA, HESSIAN_SIGMA, GRAY_THR, EIGVAL_THR):
    """提取亚像素线条中心点
    @param * 同get_subpix.param
    
    @return p 亚像素中心点，列表
    """
    #处理区域
    roi = image[xi[1]-2*WND_R : xi[1]+2*WND_R+1, xi[0]-2*WND_R : xi[0]+2*WND_R+1]
    
    #高斯平滑
    blurMask = max(np.int(2 * np.floor(3 * BLUR_SIGMA) + 1), 3)
    img = cv2.GaussianBlur(roi, (blurMask,blurMask), BLUR_SIGMA)
    #计算二维高斯核的一阶和二阶微分
    mask = np.int(np.floor(3 * HESSIAN_SIGMA))
    Gx = np.zeros((2*mask+1, 2*mask+1), dtype = np.double)
    Gy = np.zeros((2*mask+1, 2*mask+1), dtype = np.double)
    Gxx = np.zeros((2*mask+1, 2*mask+1), dtype = np.double)
    Gxy = np.zeros((2*mask+1, 2*mask+1), dtype = np.double)
    Gyy = np.zeros((2*mask+1, 2*mask+1), dtype = np.double)
    
    for i in range(-mask, mask+1):
        for j in range(-mask, mask+1):
            Gx[i+mask, j+mask] = -j*np.exp(-0.5*(i**2 + j**2) / HESSIAN_SIGMA**2) / (2.0*np.pi*HESSIAN_SIGMA**4)
            Gy[i+mask, j+mask] = -i*np.exp(-0.5*(i**2 + j**2) / HESSIAN_SIGMA**2) / (2.0*np.pi*HESSIAN_SIGMA**4)
            Gxx[i+mask, j+mask] = (j**2 - HESSIAN_SIGMA**2) * np.exp(-0.5*(i**2 + j**2) / HESSIAN_SIGMA**2) / (2.0*np.pi*HESSIAN_SIGMA**6)
            Gxy[i+mask, j+mask] = i * j * np.exp(-0.5*(i**2 + j**2) / HESSIAN_SIGMA**2) / (2.0*np.pi*HESSIAN_SIGMA**6)
            Gyy[i+mask, j+mask] = (i**2 - HESSIAN_SIGMA**2) * np.exp(-0.5*(i**2 + j**2) / HESSIAN_SIGMA**2) / (2.0*np.pi*HESSIAN_SIGMA**6)
    
    #高斯核与图像卷积作为导数
    gx = cv2.filter2D(img, -1, cv2.flip(Gx, -1), borderType = cv2.BORDER_CONSTANT)
    gy = cv2.filter2D(img, -1, cv2.flip(Gy, -1), borderType = cv2.BORDER_CONSTANT)
    gxx = cv2.filter2D(img, -1, cv2.flip(Gxx, -1), borderType = cv2.BORDER_CONSTANT)
    gxy = cv2.filter2D(img, -1, cv2.flip(Gxy, -1), borderType = cv2.BORDER_CONSTANT)
    gyy = cv2.filter2D(img, -1, cv2.flip(Gyy, -1), borderType = cv2.BORDER_CONSTANT)
    
    #提取亚像素线条中心
    p = []
    DEL_RR = DEL_R**2
    for i in range(WND_R, 3*WND_R + 1):
        for j in range(WND_R, 3*WND_R + 1):
            if img[i,j] > GRAY_THR and (i-2*WND_R)**2 + (j-2*WND_R)**2 > DEL_RR:
                hessian = np.array([[gxx[i,j], gxy[i,j]], [gxy[i,j], gyy[i,j]]], dtype = np.double)
                w, v= LA.eig(hessian)
                w = abs(w)
                d = max(w)
                vector = v[:, list(w).index(d)]
                #大于阈值，则认为是中心点
                if abs(d) > EIGVAL_THR:
                    nx, ny = vector
                    t = -(nx*gx[i,j] + ny*gy[i,j]) / (nx**2 * gxx[i,j] + 2*nx*ny*gxy[i,j] + ny**2 * gyy[i,j])
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
        c = [p.pop(0)]
        j = 0
        while j < len(c):
            t = 0
            for k in range(len(p)):
                if max([abs(round(p[k-t][0] - c[j][0])), abs(round(p[k-t][1] - c[j][1]))]) <= CONNECT_R:
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
    x0 = [2*WND_R, 2*WND_R]
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
    
    
# --------------------------------------------------------compute_H---------------------------------------------------------------
def solve_homo(p, ns):
    """计算平面到图像的单应矩阵
    @param p 图像上的点，传入的是一个列表，列表元素为array点22为矩阵
    @param ns 球上点的数目
    
    @return H 单应
    """
    N = len(p)
    # 先将图像点转化为二维数组m
    m = np.ones((3, N), dtype = np.double)
    for i in range(N):
        m[0,i] = p[i][0]
        m[1,i] = p[i][1]
        
    # 计算空间点
    M = np.ones((3, N), dtype = np.double)
    for i in range(N):
        M[0, i] = np.cos(2*(i + round(N/2))*np.pi/ns)
        M[1, i] = np.sin(2*(i + round(N/2))*np.pi/ns)
    # 归一化图像点
    ax = m[0, :]
    ay = m[1, :]
    
    mxx = np.mean(ax)
    myy = np.mean(ay)
    
    ax = ax - mxx
    ay = ay - myy
    
    scxx = np.mean(np.abs(ax))
    scyy = np.mean(np.abs(ay))
    
    Hnorm = np.array([[1/scxx, 0, -mxx/scxx], [0, 1/scyy, -myy/scyy], [0,0,1]])
    invHnorm = np.array([[scxx , 0, mxx], [0, scyy, myy], [0,0,1]])
    
    mn = Hnorm @ m
    # Compute the homography between m and mn
    # build the matix
    L = np.zeros((2*N, 9), dtype = np.double)
    L[0:2*N:2, 0:3] = M.T
    L[1:2*N:2, 3:6] = M.T
    L[0:2*N:2, 6:9] = -((np.ones((3,1)) @ mn[0:1,:]) * M).T
    L[1:2*N:2, 6:9] = -((np.ones((3,1)) @ mn[1:2,:]) * M).T
    
    L = L.T @ L
    U, S, V = LA.svd(L, full_matrices = True)
    hh = V[:, 8]
    hh = hh / hh[8]
    
    Hrem = hh.reshape((3,3))
    
    # Final homography:
    H = invHnorm @ Hrem
    
    print(H)
    '''
    # Homography refinement if there are more than 4 points
    if N > 4:
        # Final refinement
        hhv = (H.T).reshape((1,9))
        hhv = hhv[0, 0:8]
        
        for iter in range(10):
            
            mrep = H @ M
            
            J = np.zeros((2*N, 8))
            
            MMM = M/(np.ones((3,1)) @ mrep[2:3,:])
            
            J[0:2*N:2, 0:3] = -MMM.T
            J[1:2*N:2, 3:6] = -MMM.T
            
            mrep = mrep/(np.ones((3,1)) @ mrep[2:3,:])
            
            m_err = m[0:2,:] - mrep[0:2,:]
            m_err = np.array(m_err.flat)
            
            MMM2 = (np.ones((3,1)) @ mrep[0:1, :]) * MMM
            MMM3 = (np.ones((3,1)) @ mrep[1:2, :]) * MMM
            
            J[0:2*N:2, 6:8] = MMM2[0:2, :].T
            J[1:2*N:2, 6:8] = MMM3[0:2, :].T
            
            MMM = (M /(np.ones((3,1)) @ mrep[2:3, :])).T
            hh_innov = np.linalg.inv(J.T @ J) @ J.T @ m_err
            hhv_up = hhv - hh_innov
            
            temp = list(hhv_up)
            temp.append(1.0)
            hhv_up_p = np.array(temp, dtype = np.double)
            
            H_up = hhv_up_p.reshape((3,3)).T
            
            hhv = hhv_up
            H = H_up
            
    print(H)
    '''
    #验证
    A = np.zeros((2, 6), dtype = np.double)
    getV = lambda H, i, j: np.array([H[0,i]*H[0,j], H[0,i]*H[1,j] + H[1,i]*H[0,j], H[1,i]*H[1,j], H[2,i]*H[0,j] + H[0,i]*H[2,j],\
    H[2,i]*H[1,j] + H[1,i]*H[2,j], H[2,i]*H[2,j]])
    A[0, :] = getV(H, 0, 1)
    A[1, :] = getV(H, 0, 0) - getV(H, 1, 1)
    
    #标准
    K = np.array([[5114,0,831], [0,5114,608], [0,0,1]], dtype = np.double)
    KKT = LA.inv(K@K.T)
    MZZY = np.array([[KKT[0,0], KKT[0,1], KKT[1,1], KKT[0,2], KKT[1,2], KKT[2,2]]], dtype = np.double)
    print("残差:")
    print(A@MZZY.T)
    return H
    
#---------------------------------------------------------calibrate-----------------------------------------------------
def solve_K(Hs):
    """计算内参
    @param Hs 包含单应的列表
    
    @return K 摄像机内参
    """
    N = len(Hs)
    A = np.zeros((2*N, 6), dtype = np.double)
    getV = lambda H, i, j: np.array([H[0,i]*H[0,j], H[0,i]*H[1,j] + H[1,i]*H[0,j], H[1,i]*H[1,j], H[2,i]*H[0,j] + H[0,i]*H[2,j],\
    H[2,i]*H[1,j] + H[1,i]*H[2,j], H[2,i]*H[2,j]])
    for i in range(N):
        A[2*i, :] = getV(Hs[i], 0, 1)
        A[2*i + 1, :] = getV(Hs[i], 0, 0) - getV(Hs[i], 1, 1)
    U, S, V = LA.svd(A, full_matrices=1)
    w = np.array([[V[0,5], V[1,5], V[3,5]], [V[1,5], V[2,5], V[4,5]], [V[3,5], V[4,5], V[5,5]]])
    w_ = LA.inv(w)
    w_ = w_/w_[2,2]
    ux = w_[0,2]
    uy = w_[1,2]
    fx = np.sqrt(w_[0,0] - ux*ux)
    fy = np.sqrt(w_[1,1] - uy*uy)
    K = np.array([[fx, 0, ux], [0, fy, uy], [0, 0, 1.0]], dtype = np.double)
    
    return K