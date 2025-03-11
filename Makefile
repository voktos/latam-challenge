.ONESHELL:

format:
	@poetry run black src/ tests/

lint:
	@poetry run pflake8 src/ tests/

test:
	@export PYTHONPATH="./src:$$PYTHONPATH"
	@poetry run coverage run -m unittest discover -s tests/
	@poetry run coverage report -m --fail-under=100

dependencies:
	@poetry export --without-hashes --with dev,test --format requirements.txt > requirements.txt
