.PHONY: clean setup clean-python-deps run lint isort isort-autofix

PYTHON_DIRS := condobus/ org/ transport/

clean:
	@find . -name "*.pyc" -delete

setup:
	@pip install -r requirements-test.txt

clean-python-deps:
	@pip freeze | grep -v "^-e" | xargs pip uninstall -y

run: clean
	@./manage.py runserver

lint: clean
	@flake8 .

isort: clean
	isort --recursive --check-only --diff ${PYTHON_DIRS}

isort-autofix: clean
	@isort --recursive --atomic ${PYTHON_DIRS}
