# -*- coding: utf-8 -*-

import numpy as np
from numba import jit, float64, int32, double, void, njit
import numba as nb

class ImageAlter():
    def crop(img):
        l1, w1, ch = np.shape(img)
        k =0
        t =0
        k1 =0
        t1 =0
        for i in range(0,int(w1/2)):
            if img[int(l1/2),i,0]!=255 or  img[int(l1/2),i,1]!=255 or  img[int(l1/2),i,2]!=255:
                k = i
                #print(k)
                break
        for i in range(0,int(l1/2)):
            if img[i,int(w1/2),0]!=255 or  img[i,int(w1/2),1]!=255 or  img[i,int(w1/2),2]!=255:
                t = i
                #print(t)
                break
        
        for i in range(1,int(w1/2)):
            if img[int(l1/2),w1-i,0]!=255 or  img[int(l1/2),w1-i,1]!=255 or  img[int(l1/2),w1-i,2]!=255:
                k1 = w1-i-1
                #print(k1)
                break
        for i in range(1,int(l1/2)):
            if img[l1-i,int(w1/2),0]!=255 or  img[l1-i,int(w1/2),1]!=255 or  img[l1-i,int(w1/2),2]!=255:
                t1 = l1-i-1
                #print(t1)
                break
        img2 = img[t:t1,k:k1,:] 
        return img2
#    @jit(nopython =True)
    def maxRepeating(img, num): 
        count = np.zeros([num])
        for i in range(0, 9):
            for j in range(0, num):
                if img[i]==j:
                    count[j]= count[j]+1
        
      
        result = max(count)
        ind  = np.argmax(count)
        return result, ind
#    @jit(nopython =True)
    def enhancing(img, clus_num):
        vec = np.zeros([3,3])
        l1, w1 = np.shape(img)
        for i in range(1,l1-1):
            for j in range(1, w1-1):
                vec[:,:] = img[i-1:i+2,j-1:j+2]
                vec1 = vec.reshape((9)) 
                result, ind = ImageAlter.maxRepeating(vec1,   clus_num) 
                if result > 3:
                    img[i,j] = ind
        return img
    @njit
    def dist1(x,y):
        z = np.sqrt(1*(x[0]-y[0])**2 +1*(x[1]-y[1])**2+ 1*(x[2]-y[2])**2)
        return z
    @njit
    def dist2(x,y):
        z = np.sqrt((x[0]-y[0])**2 +(x[1]-y[1])**2)
        return z
    @njit
    def dist1_w(x,y):
        z = np.sqrt(1.4*(x[0]-y[0])**2 +(x[1]-y[1])**2+ (0.6*(x[2]-y[2])**2))
        return z
    @njit
    def dist_v(x,y):
        z = np.sqrt(0*(x[0]-y[0])**2 +0*(x[1]-y[1])**2+ (1*(x[2]-y[2])**2))
        return z