default: yapf lint test

lint:
	poetry run pylint thailand_geography tests

test:
	cd tests && poetry run python manage.py test

coverage:
	poetry run coverage erase
	poetry run coverage run --source='thailand_geography' tests/manage.py test tests
	poetry run coverage report -m

yapf:
	poetry run yapf -ipr thailand_geography tests
