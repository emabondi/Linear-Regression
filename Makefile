all: init

init:
	pip install pipenv
	pipenv install
	pipenv shell

train:
	python3 train.py

clean:
	rm -rf  thetas.csv
	rm -rf	rmse_plot.png
	rm -rf	result.png	

fclean: clean
		rm -rf Pipfile.lock