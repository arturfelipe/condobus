.PHONY: clean setup clean-python-deps run

clean:
	@find . -name "*.pyc" -delete

setup:
	@pip install -r requirements-test.txt

clean-python-deps:
	@pip freeze | grep -v "^-e" | xargs pip uninstall -y

run: clean
	@./manage.py runserver
