import csv

#def calculate_tetha1(tetha0):
#	with open('data.csv', mode ='r')as file:
#		csvFile = csv.reader(file)
#		count = 0
#		sum = 0
#		for lines in csvFile:
#			if (lines[0] == 'km'):
#				continue
#			count += 1
#			tetha1 = (tetha0 - int(lines[1])) / int(lines[0])
#			sum += tetha1
#		return sum/count

def main():
	theta0 = 20000
	#theta1 = calculate_tetha1(theta0)
	theta1 = -0.116

	mileage = input("Insert a mileage to predict car price: ")
	while not mileage.isnumeric():
		mileage = input("Insert a numeric mileage: ")
	mileage = int(mileage)
	prediction = theta0 + (theta1 * mileage)
	print ('Predicted price: ', end='')
	print(prediction)

if __name__ == "__main__":
	main()

#65
#36
#33
#41
#33