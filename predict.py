import os

def estimatePrice(mileage, theta0, theta1):
	return theta0 + (theta1 * mileage)

def main():
	theta0 = 0
	theta1 = 0

	if os.path.isfile('thetas.csv'):
		with open('thetas.csv', 'r') as f:
			theta0 , theta1 = f.read().split(',')
			theta0 = float(theta0)
			theta1 = float(theta1)

	mileage = input("Insert a mileage to predict car price: ")
	while not mileage.isnumeric():
		mileage = input("Insert a numeric mileage: ")
	mileage = int(mileage)

	prediction = estimatePrice(mileage, theta0, theta1)
	print (f'Predicted price: {prediction}')

if __name__ == "__main__":
	main()
