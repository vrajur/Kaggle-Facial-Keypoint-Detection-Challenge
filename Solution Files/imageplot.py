import matplotlib.pyplot as plt
import pylab

import numpy as np

def plot(im):
	image = np.reshape(im,(96,96))
	plt.imshow(im, cmap="Greys_r")
	pylab.show()
	
