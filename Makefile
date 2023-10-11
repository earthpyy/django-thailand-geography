default: yapf lint test

lint:
	poetry run pylint thailand_geography

test:
	poetry run python manage.py test

coverage:
	poetry run coverage erase
	poetry run coverage run --source='thailand_geography' manage.py test
	poetry run coverage report -m

yapf:
	poetry run yapf -ipr thailand_geography --exclude '**/migrations/*.py'

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
