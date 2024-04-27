import pandas as pd

from matplotlib import pyplot as plt
from predict import estimatePrice


def plot(x, y, theta0, theta1):
	plt.plot(x, y, 'ro', markersize=4)
	plt.plot(x, theta0 + theta1 * x, 'b')
	plt.xlabel('Mileage')
	plt.ylabel('Price')
	plt.show()

def normalize(x):
	return (x - x.min()) / (x.max() - x.min())

def train():
	theta0 = 0.0
	theta1 = 0.0
	learningRate = 0.01
	epochs = 10000
	df = pd.read_csv('data.csv').astype(float)
	x, y = df.iloc[:, 0].values, df.iloc[:, 1].values

	print(type(x))
	x_norm = normalize(x)
	y_norm = normalize(y)


	for j in range(epochs):
		m = len(x)
		tmp0 = 0
		tmp1 = 0
		for i in range(m):
			tmp0 += estimatePrice(x_norm[i], theta0, theta1) - y_norm[i]
			tmp1 += (estimatePrice(x_norm[i], theta0, theta1) - y_norm[i]) * x_norm[i]
		
		theta0 -= (learningRate / m) * tmp0
		theta1 -= (learningRate / m) * tmp1

	plot(x_norm, y_norm, theta0, theta1)

	theta0 = theta0 * (y.max() - y.min()) + y.min() - theta1 * x.min() * (y.max() - y.min()) / (x.max() - x.min())
	theta1 = theta1 * (y.max() - y.min()) / (x.max() - x.min())
	
	plot(x, y, theta0, theta1)

	print(f'theta0:{theta0}  theta1:{theta1}' )
	with open('thetas.csv', 'w') as f:
		f.write("{},{}".format(theta0, theta1))



if __name__ == "__main__":
	train()