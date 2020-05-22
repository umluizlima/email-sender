.PHONY: install
install:
	pip install -r requirements-dev.txt && \
	pre-commit install

.PHONY: test
test:
	PYTHONPATH=. \
	python -m pytest --cov=app
