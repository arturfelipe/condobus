.PHONY: clean setup lint

clean:
	@find . -name "*.pyc" -delete

setup:
	@pip install -r requirements-test.txt

run: clean
	@./manage.py runserver
