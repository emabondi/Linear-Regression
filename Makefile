all: init

init:
	pip install pipenv
	pipenv install
	pipenv shell

clean:
	rm -rf  thetas.csv
	

fclean: clean
		rm -rf Pipfile.lock