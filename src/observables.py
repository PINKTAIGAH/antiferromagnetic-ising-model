import numpy as np

class Observables(object):

    def __init__(self, J=-1, kT=1, l=50, tau= 10000, h0= 10, P= 25):

        self.P= P
        self.tau= tau
        self.h0= h0
        self.kT= kT
        self.J= J
        self.indices= np.indices((50,50))+1
        self.y= self.indices[0]
        self.x= self.indices[1]
        self.exponentials= self.y+self.x
        self.sgn= -np.ones((l,l))
        self.findSgn()
        
    def findSgn(self):
        
        self.exponentials= self.y+self.x
        for i in np.ndindex((50, 50)):
            
            self.sgn[i]= self.sgn[i]**self.exponentials[i]     
    
    def findMagnetisation(self, arr):

        return arr.sum()
    
    def findMagnetisationStaggered(self, arr):

        staggeredMag= self.sgn*arr
        return staggeredMag.sum()
    
    def findEnergy(self, arr, h):
        
        E= -self.J*arr*(np.roll(arr, +1, axis=0) +\
                        np.roll(arr, -1, axis=0) +\
                        np.roll(arr, +1, axis=1) +\
                        np.roll(arr, -1, axis=1)) -\
                        h * arr
        return E.sum()

    def findAverage(self, arr):
    
        return np.average(np.absolute(arr))
    
    def findVariance(self, arr):
        
        return (np.average(np.array(arr)**2) - np.average(arr)**2)/2500
    
    def findField(self, t):

        return  self.h0* np.cos(2*np.pi*self.x/self.P) * \
                np.cos(2*np.pi*self.y/self.P) * \
                np.cos(2*np.pi*t/self.tau)
