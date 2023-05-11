import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

class Animate(object):
#===========================================================
# Animate a simulation that returns an image without tying matplotlib to 
# simulation steps.

    def __init__(self, initialFrame, cmap='gnuplot'):
    #=======================================================
    # Initialise figure and inital frame of animation

        self.cmap= cmap
        self.fig= plt.figure()
        self.im= plt.imshow(initialFrame, animated=True, cmap= self.cmap)
        plt.colorbar()
    
    def drawImage(self, lattice_array):
    #=======================================================
    # Draw frame of the animation

        plt.cla()
        self.im= plt.imshow(lattice_array, animated= True, cmap= self.cmap)
        plt.draw()
        plt.pause(0.0001)

