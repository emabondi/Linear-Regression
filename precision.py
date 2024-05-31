import pandas as pd
import os
import numpy as np

from predict import estimatePrice


def precision(y, y_hat):
	return 1 - (np.sum(np.abs(y - y_hat)) / np.sum(y))

def pprecision():
	try:
		df = pd.read_csv('data.csv').astype(float)
	except FileNotFoundError:
		print('data.csv does not exist, aborting.')
		return
	except pd.errors.EmptyDataError:
		print('data.csv file is empty, aborting.')
		return
	x, y = df.iloc[:, 0].values, df.iloc[:, 1].values

	if os.path.isfile('thetas.csv'):
		with open('thetas.csv', 'r') as f:
			theta0 , theta1 = f.read().split(',')
			theta0 = float(theta0)
			theta1 = float(theta1)
	else:
		print('missing thetas.csv, aborting.')
		return
	
	print(f'precision:{precision(y, estimatePrice(x, theta0, theta1)) * 100:.2f}%\n')

if __name__ == "__main__":
	pprecision()