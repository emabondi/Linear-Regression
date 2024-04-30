import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from predict import estimatePrice

def rmse_plot(y):
	plt.title('Error curve (root mean squared error)')
	plt.plot(y, 'b')
	plt.xlabel('Epochs')
	plt.ylabel('RMSE')
	plt.show()
	plt.savefig('rmse_plot.png')

def plot(x, y, theta0='none', theta1='none'):
	plt.xlabel('Mileage')
	plt.ylabel('Price')
	plt.plot(x, y, 'ro', markersize=4)
	if theta0 != 'none':
		plt.plot(x, theta0 + theta1 * x, 'b')
		plt.savefig('result.png')
	plt.show()

def errorPercentage(y, y_hat):
	return np.sum(np.abs(y - y_hat) / y * 100) / len(y)

def rootMeanSquaredError(y, y_hat):
	n = len(y)
	return np.sqrt((1 / n) * np.sum((y - y_hat)**2))

def precision(y, y_hat):
	return 1 - (np.sum(np.abs(y - y_hat)) / np.sum(y))

def normalize(x):
	return (x - x.min()) / (x.max() - x.min())

def train():
	theta0 = 0.0
	theta1 = 0.0
	learningRate = 0.01
	epochs = 15000
	try:
		df = pd.read_csv('data.csv').astype(float)
	except FileNotFoundError:
		print('data.csv does not exist, aborting.')
		return
	except pd.errors.EmptyDataError:
		print('data.csv file is empty, aborting.')
		return
	x, y = df.iloc[:, 0].values, df.iloc[:, 1].values
	plot(x, y)

	x_norm = normalize(x)
	y_norm = normalize(y)

	errors = []

	for j in range(epochs):
		m = len(x)
		tmp0 = 0
		tmp1 = 0
		for i in range(m):
			tmp0 += estimatePrice(x_norm[i], theta0, theta1) - y_norm[i]
			tmp1 += (estimatePrice(x_norm[i], theta0, theta1) - y_norm[i]) * x_norm[i]
		
		theta0 -= (learningRate / m) * tmp0
		theta1 -= (learningRate / m) * tmp1
		m = rootMeanSquaredError(y_norm, estimatePrice(x_norm, theta0, theta1))
		errors.append(m)

	rmse_plot(errors)

	theta0 = theta0 * (y.max() - y.min()) + y.min() - theta1 * x.min() * (y.max() - y.min()) / (x.max() - x.min())
	theta1 = theta1 * (y.max() - y.min()) / (x.max() - x.min())
	
	plot(x, y, theta0, theta1)

	print(f'rootMeanSquaredError:{rootMeanSquaredError(y, estimatePrice(x, theta0, theta1))}\n')
	
	print(f'precision:{precision(y, estimatePrice(x, theta0, theta1)) * 100:.2f}%\n')

	print(f'error percentage:{errorPercentage(y, estimatePrice(x, theta0, theta1)):.2f}%\n')
 
	print(f'theta0: {theta0}  theta1: {theta1}' )
	with open('thetas.csv', 'w') as f:
		f.write("{},{}".format(theta0, theta1))



if __name__ == "__main__":
	train()