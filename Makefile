.PHONY: clean setup clean-python-deps run lint

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
