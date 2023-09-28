install:
	poetry install

lint:
	poetry run black .

check:
		poetry run black . --check

test:
	$(MAKE) lint
	poetry run pytest

test-watch:
	poetry run ptw
