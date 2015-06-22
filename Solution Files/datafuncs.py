import numpy as np
import pandas as pd 

def data2array(data, fieldx, fieldy): 

	x_list = data[fieldx]
	y_list = data[fieldy]
	id_list = data['id']
	
	idx = ~pd.isnull(y_list)
	
	x_arr = np.array(map(float, x_list[idx]))
	y_arr = np.array(map(float, y_list[idx]))
	id_arr = np.array(id_list[idx])
	
	arr = zip(x_arr, y_arr, id_arr)
	
	raise Exception("Figure out INDEXING!!!!")
	
	return arr
	
	
	
	
# def data2array(data, field):
	# if field != 'Image':
		
		# x_list = data[field+'_x']
		# y_list = data[field+'_y']
		
		# x_list = x_list[~pd.isnull(y_list)]
		# y_list = y_list[~pd.isnull(y_list)]
		
		# x_arr = np.array(map(float, x_list))
		# y_arr = np.array(map(float, y_list))
		
		# arr = zip(x_arr, y_arr)
		
		# return (arr)
		
	# else:
		# list = data[field]
		# list = list[~pd.isnull(list)]
		
		# arr = np.fromstring(list, sep=' ')
		
		# #arr = [np.fromstring(x,sep=' ') for x in list if not pd.isnull(x)]

		# return arr