'''
Created on 2016年4月5日

@author: tanke
'''
import numpy as np

def compute_homography(corner, N, ns):
    '''计算平面到图像的单应矩阵
    @param corner 图像上的点，传入的是一个列表，列表元素为array点
    @param N 计算单应的图像点数
    @param ns 球上点的数目
    '''
    # 先将图像点转化为二维数组m
    m = np.ones((3, N), dtype = np.double)
    for i in range(N):
        m[0,i] = corner[i][0]
        m[1,i] = corner[i][1]
        
    # 计算空间点
    M = np.ones((3, N), dtype = np.double)
    for i in range(N):
        M[0, i] = np.cos(2*i*np.pi/ns)
        M[1, i] = np.sin(2*i*np.pi/ns)
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
    
    mn = np.dot(Hnorm, m)
    # Compute the homography between m and mn
    # build the matix
    L = np.zeros((2*N, 9), dtype = np.double)
    L[0:2*N:2, 0:3] = M.T
    L[1:2*N:2, 3:6] = M.T
    L[0:2*N:2, 6:9] = -(np.dot(np.ones((3,1)), mn[0,:]) * M).T
    L[1:2*N:2, 6:9] = -(np.dot(np.ones((3,1)), mn[1,:]) * M).T
    
    L = np.dot(L.t, L)
    U, S, V = np.linalg.svd(L, full_matrices = True)
    hh = V[:, 8]
    hh = hh / hh[8]
    
    Hrem = hh.reshape((3,3))
    
    # Final homography:
    H = np.dot(invHnorm, Hrem)
    
    # Homography refinement if there are more than 4 points
    if N > 4:
        # Final refinement
        hhv = (H.T).reshape((9,1))
        hhv = hhv[0:8]
        
        for iter in range(10):
            
            mrep = np.dot(H, M)
            
            J = np.zeros(2*N, 8)
            
            MMM = M/(np.dot(np.ones((3,1)), mrep[2,:]))
            
            J[0:2*N:2, 0:3] = -MMM.T
            J[1:2*N:2, 3:6] = -MMM.T
            
            mrep = mrep/np.dot(np.ones((3,1)), mrep[2,:])
            
            m_err = m[0:2,:] - mrep[0:2,:]
            #m_err = m_err[:]
            
            
            
    
    