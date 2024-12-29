install:
	poetry install --with dev

format:
	poetry run ruff format

lint:
	poetry run ruff check --fix

test:
	poetry run pytest --cov .
