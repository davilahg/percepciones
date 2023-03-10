import pandas as pd
import numpy as np
import math

df = pd.read_csv('m4.csv', index_col = 0)

def MA_a_enlaces(df):
		n1 = []
		n2 = []
		enlaces = []
		df = df.to_numpy()
		for i in np.arange(df.shape[0]):
			for j in np.arange(df.shape[1]):
				if not(math.isnan(df[i,j])):
					n1.append(i)
					n2.append(j)
					enlaces.append(df[i,j])
		enlaces_df = pd.DataFrame(list(zip(n1,n2,enlaces)), columns = ['n1','n2','enlaces'])
		return enlaces_df




enlaces_1 = MA_a_enlaces(df)
enlaces_2 = MA_a_enlaces(df)
enlaces_3 = MA_a_enlaces(df)
enlaces_4 = MA_a_enlaces(df)

enlaces_1.to_csv('enlaces_m1.csv', index = False)
enlaces_2.to_csv('enlaces_m2.csv', index = False)
enlaces_3.to_csv('enlaces_m3.csv', index = False)
enlaces_4.to_csv('enlaces_m4.csv', index = False)


