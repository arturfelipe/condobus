.PHONY: clean setup-frontend setup-backend setup clean-python-deps run-backend run-frontend migrate test-backend lint-backend isort isort-autofix db-setup db-cleanup db-seed

PYTHON_DIRS := condobus/ org/ transport/

clean:
	@find . -name "*.pyc" -delete

setup-frontend:
	@npm i --prefix client

setup-backend:
	@pip install -r requirements-test.txt

setup: setup-backend setup-frontend

clean-python-deps:
	@pip freeze | grep -v "^-e" | xargs pip uninstall -y

run-backend: clean
	@./manage.py runserver 0.0.0.0:8000

run-frontend: clean
	@npm start --prefix client

migrate: clean
	@./manage.py migrate

test-backend: clean
	@./manage.py test

lint-backend: clean
	@flake8 .

isort: clean
	@isort --recursive --check-only --diff ${PYTHON_DIRS}

isort-autofix: clean
	@isort --recursive --atomic ${PYTHON_DIRS}

db-setup:
	# Add you postgres user with the -U option in the end of the commands below
	@psql -c "CREATE DATABASE condobus;" -d postgres
	@psql -c "CREATE USER condobus WITH PASSWORD 'condobus' SUPERUSER;" -d condobus
	@psql -c "CREATE EXTENSION postgis;" -d condobus

db-cleanup:
	@dropdb condobus
	@dropuser condobus

db-seed:
	@./manage.py loaddata db.json
