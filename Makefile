.PHONY: clean setup clean-python-deps run lint isort isort-autofix db-setup db-cleanup db-seed

PYTHON_DIRS := condobus/ org/ transport/

clean:
	@find . -name "*.pyc" -delete

setup:
	@pip install -r requirements-test.txt

clean-python-deps:
	@pip freeze | grep -v "^-e" | xargs pip uninstall -y

run: clean
	@./manage.py runserver

test: clean
	@./manage.py test

lint: clean
	@flake8 .

isort: clean
	isort --recursive --check-only --diff ${PYTHON_DIRS}

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
