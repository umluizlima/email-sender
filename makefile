.PHONY: install
install:
	pip install -r requirements-dev.txt && \
	pre-commit install
