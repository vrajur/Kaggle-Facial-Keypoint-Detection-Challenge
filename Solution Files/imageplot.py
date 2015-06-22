import matplotlib.pyplot as plt
import pylab

import numpy as np


# Plot an Image:
def plot(im):
	image = np.reshape(im,(96,96))
	plt.imshow(image, cmap="Greys_r")
	pylab.show()
	

# Cycle through a range of Images:
def cycler(idStart, idEnd, featureIDs):	
	plt.interactive(True)
	for i in range(idStart, idEnd):
		plot(Image[imID[i]])
		input_txt = "{0}) Image ID: {1}".format(i,imID[i])
		useless = raw_input(input_txt)
		for fid in featureIDs:
			if fid != -1:
				t = train[features[fid]][i]
				im = np.reshape(Image[imID[i]], (96,96))
				fs = (13,21)								# feature size (aka size of pixel box containing feature)
				ir = [t[1] - fs[0]/2, t[1] + fs[0]/2+1]		# boundaries for slicing (in rows direction)
				ic = [t[0] - fs[1]/2, t[0] + fs[1]/2+1]		# boundaries for slicing (in cols direction)
				piece2 = im[ir[0]:ir[1], ic[0]:ic[1]]
				plt.interactive(True)
				plt.imshow(piece2, cmap="Greys_r")
				input_txt = "\tFeature: {0}".format(features[fid])
				useless = raw_input(input_txt)
	plt.close()
	

	
# Method for slicing specific features out of image
t = train[features[j]][i]
im = np.reshape(Image[imID[i]], (96,96))
fs = (13,21)								# feature size (aka size of pixel box containing feature)
ir = [t[1] - fs[0]/2, t[1] + fs[0]/2+1]		# boundaries for slicing (in rows direction)
ic = [t[0] - fs[1]/2, t[0] + fs[1]/2+1]		# boundaries for slicing (in cols direction)

piece2 = im[ir[0]:ir[1], ic[0]:ic[1]]

		