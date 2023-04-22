build: venv migrate runserver

venv:
	pip3 install pipenv
	pipenv install -r requirements.txt
	
migrate:
	pipenv run python  manage.py migrate

runserver:
	pipenv run python  manage.py runserver

clean:
	pipenv --rm
	
