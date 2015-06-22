import numpy as np
import pandas as pd

import datafuncs as df

# Load data from csv:
data = pd.read_csv('../Data/training.csv') 		# 'training.csv'
data['id'] = range(len(data))					# add id column


# Labels:
labels = np.asarray(data.axes[1])				# Convert to numpy array
feature_labels = labels[:-2]					# All labels except 'Image' and 'id'

train = {}										# Training Example Dictionary
features = []									# Array of Features

# Construct Training Example Dictionary:
for i in range(0,len(feature_labels),2):
	label = [feature_labels[i], feature_labels[i+1]]
	features.append(label[1][:-2])
	train[features[-1]] = df.data2array(data, label[0], label[1])

	
# Construct Image ID Dictionary:
Image = {}
imID = []

image = data['Image']


for i,im in enumerate(image):
	if not pd.isnull(im):
		Image[i] = np.fromstring(im, sep=' ')
		imID.append(i)
		diff = len(Image[i]) - 96**2
		if diff > 0:									# If Image array is larger than 96x96 pixels
			Image[i] = Image[i][:-diff]					# Take the First 96**2 pixels
		elif diff < 0:									# If Image array is smaller than 96x96 pixels
			add = np.zeros((-diff))						
			Image[i] = np.hstack((Image[i], add))		# Fill missing pixels with 0's
			
			




 

# # Separate image data:
# image = data['Image']

# #image_clean = filter((lambda im: not pd.isnull(im)), image)
# #image_array = map((lambda im: np.fromstring(im, sep=' ')), image_clean)

# # Convert Images Data to Array:
# image_arr = [np.fromstring(x,sep=' ') for x in image if not pd.isnull(x)]

# # Count Data Example Size:
# #data.count()

# # Reduce Data to Examples with all Data:
# data_full = data.dropna()				# 2140 examples











	
	
