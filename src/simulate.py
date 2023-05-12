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
        self.observables= Observables()
    
    def generateInitLattice(self):

        self.arr= np.random.choice(np.array([1,-1]), size=(self.l, self.l))

    def runSimulationVisualisation(self):

        self.epoch= 0
        self.sweeps= 0       
        self.algorithm= Algorithms(self.l, self.h)
        
        self.generateInitLattice()
        self.animation= Animate(self.arr, 'binary')
        
        while True:
            self.arr= self.algorithm.updateStepConst(self.arr)
            self.epoch+=1

            if self.epoch % self.N == 0:
                self.sweeps+= 1
                print(self.sweeps)
                self.animation.drawImage(self.arr)

    def runSimulationMagnetisationSingle(self):
        
        self.epoch= 0
        self.sweeps= 1 
        self.magnetisationArray= []
        self.energyArray= []
        self.magnetisationStaggeredArray= []
        self.algorithm= Algorithms(self.l, self.h)

        while True:
            self.arr= self.algorithm.updateStep(self.arr)
            self.epoch+=1
            
            if self.epoch % self.N == 0:
                self.sweeps+= 1
                self.magnetisationArray.append(self.observables.findMagnetisation(self.arr))
                self.energyArray.append(self.observables.findEnergy(self.arr, self.h))
                self.magnetisationStaggeredArray.append(self.observables.findMagnetisationStaggered(self.arr))
            
            if self.sweeps % 100 ==0:
                print(f'The mean magnetisation is {self.observables.findAverage(self.magnetisationArray[100:])}')
                print(f'The mean variance is {self.observables.findVariance(self.magnetisationArray[100:])}')
                print(f'The mean energy is {self.observables.findAverage(self.energyArray[100:])}')
                print(f'The mean magnetisation staggered is {self.observables.findAverage(self.magnetisationStaggeredArray[100:])}')
                print(f'The mean magnetisation staggered variance is {self.observables.findVariance(self.magnetisationStaggeredArray[100:])}')
                break

    def runSimulationMagnetisationRange(self):
        
        self.magFields= np.arange(0,10.5, 0.5)
        self.algorithm= Algorithms(self.l, self.h)
        
        self.magnetisationAverage=[]
        self.energyAverage=[]
        self.magnetisationStaggeredAverage= []
        self.magnetisationVariance=[]
        self.magnetisationStaggeredVariance=[]

        for i in range(self.magFields.size):
            self.epoch= 0
            self.sweeps= 1
            self.h= self.magFields[i]
            self.magnetisationArray= []
            self.energyArray= []
            self.magnetisationStaggeredArray= []

            print(i)
            while True:
                self.arr= self.algorithm.updateStepConst(self.arr)
                self.epoch+=1
                
                if self.epoch % self.N == 0:
                    self.sweeps+= 1
                    self.magnetisationArray.append(self.observables.findMagnetisation(self.arr))
                    self.energyArray.append(self.observables.findEnergy(self.arr, self.h))
                    self.magnetisationStaggeredArray.append(self.observables.findMagnetisationStaggered(self.arr))
                
                if self.sweeps % 200==0:
                    self.magnetisationAverage.append(self.observables.findAverage(self.magnetisationArray))
                    self.energyAverage.append(self.observables.findAverage(self.energyArray))
                    self.magnetisationStaggeredAverage.append(self.observables.findAverage(self.magnetisationStaggeredArray))
                    self.magnetisationVariance.append(self.observables.findVariance(self.magnetisationArray))
                    self.magnetisationStaggeredVariance.append(self.observables.findVariance(self.magnetisationStaggeredArray))
                    break
        np.savetxt(f'../Data/magnetisation_data.txt', np.array([self.magFields, self.magnetisationAverage, self.energyAverage, \
                                                                    self.magnetisationStaggeredAverage,self.magnetisationVariance, \
                                                                    self.magnetisationStaggeredVariance]).T)
        

    def runSimulationVariableH(self, P, tau, h0):

        self.epoch= 0
        self.sweeps= 0       
        self.algorithm= Algorithms(self.l, self.h)
        self.observables= Observables(P=P, tau=tau, h0=h0)
        
        self.generateInitLattice()
        self.animation= Animate(self.arr, 'binary')
        
        while True:
            self.h= self.observables.findField(self.sweeps)
            self.arr= self.algorithm.updateStepVariable(self.arr, self.h)
            self.epoch+=1

            if self.epoch % self.N == 0:
                self.sweeps+= 1
                print(self.sweeps)
                self.animation.drawImage(self.arr)

if __name__== '__main__':

    # Visualise
    # simulation= Simulate(50, 8)
    # simulation.runSimulationVisualisation()

    # part 2
    simulation= Simulate(50, 0)
    simulation.runSimulationMagnetisationRange()

    # part 3
    # simulation= Simulate(50, 0)
    # simulation.runSimulationVariableH(25, 10000, 10)
