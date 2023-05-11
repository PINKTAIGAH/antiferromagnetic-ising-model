import numpy as np
from animate import Animate
from algorithms import Algorithms
from observables import Observables

class Simulate(object):

    def __init__(self, l, h):

        self.l= l
        self.h= h
        self.N= l**2
        self.generateInitLattice()
    
    def generateInitLattice(self):

        self.arr= np.random.choice(np.array([1,-1]), size=(self.l, self.l))

    def runSimulationVisualisation(self):

        self.epoch= 0
        self.sweeps= 0       
        self.algorithm= Algorithms(self.l, self.h)
        
        self.generateInitLattice()
        self.animation= Animate(self.arr, 'binary')
        
        while True:
            self.arr= self.algorithm.updateStep(self.arr)
            self.epoch+=1

            if self.epoch % self.N == 0:
                self.sweeps+= 1
                print(self.sweeps)
                self.animation.drawImage(self.arr)

if __name__== '__main__':

    # Visualise
    simulation= Simulate(50, 8)
    simulation.runSimulationVisualisation()
