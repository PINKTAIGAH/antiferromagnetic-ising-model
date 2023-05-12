import numpy as np

class Algorithms(object):

    def __init__(self,l ,h, kT=1, J=-1):
        
        self.l= l
        self.h= h
        self.kT= kT
        self.J= J

    def generateRandCoord(self):

        self.coords= tuple(np.random.randint(0, high= self.l, size= 2))
    
    def findDeltaEConstH(self):

        self.sCenter= self.arr[self.coords]
        self.sCenterFlip= -self.sCenter
        initE= -self.J*self.sCenter*(np.roll(self.arr, +1, axis=0)[self.coords] +\
                                         np.roll(self.arr, -1, axis=0)[self.coords] +\
                                         np.roll(self.arr, +1, axis=1)[self.coords] +\
                                         np.roll(self.arr, -1, axis=1)[self.coords]) -\
                                         self.h * self.sCenter
        
        finalE= -self.J*self.sCenterFlip*(np.roll(self.arr, +1, axis=0)[self.coords] +\
                                            np.roll(self.arr, -1, axis=0)[self.coords] +\
                                            np.roll(self.arr, +1, axis=1)[self.coords] +\
                                            np.roll(self.arr, -1, axis=1)[self.coords]) -\
                                            self.h * self.sCenterFlip
                                            
        self.deltaE= finalE-initE
    

    def findDeltaEVariableH(self):

        self.sCenter= self.arr[self.coords]
        self.sCenterFlip= -self.sCenter
        initE= -self.J*self.sCenter*(np.roll(self.arr, +1, axis=0)[self.coords] +\
                                         np.roll(self.arr, -1, axis=0)[self.coords] +\
                                         np.roll(self.arr, +1, axis=1)[self.coords] +\
                                         np.roll(self.arr, -1, axis=1)[self.coords]) -\
                                         self.h[self.coords] * self.sCenter
        
        finalE= -self.J*self.sCenterFlip*(np.roll(self.arr, +1, axis=0)[self.coords] +\
                                            np.roll(self.arr, -1, axis=0)[self.coords] +\
                                            np.roll(self.arr, +1, axis=1)[self.coords] +\
                                            np.roll(self.arr, -1, axis=1)[self.coords]) -\
                                            self.h[self.coords] * self.sCenterFlip
        
        self.deltaE= finalE-initE
    
    def applyChange(self):

        if self.deltaE <= 0:
            self.arr[self.coords]= self.sCenterFlip

        elif np.random.rand() < np.exp(-self.deltaE/self.kT):
            self.arr[self.coords]= self.sCenterFlip

    def updateStepConst(self, arr):
        
        self.arr= arr
        self.generateRandCoord()
        self.findDeltaEConstH()
        self.applyChange()
        return self.arr
    
    def updateStepVariable(self, arr, h):
        
        self.h= h
        self.arr= arr
        self.generateRandCoord()
        self.findDeltaEVariableH()
        self.applyChange()
        return self.arr