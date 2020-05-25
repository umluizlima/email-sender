.PHONY: install
install:
	pip install -r requirements-dev.txt && \
	pre-commit install

.PHONY: broker_init
broker_init:
	docker-compose up -d broker

.PHONY: test
test:
	PYTHONPATH=. \
	python -m pytest --cov=app

.PHONY: run_worker
run_worker: broker_init
	celery -A app.worker worker --loglevel debug

.PHONY: run
run:
	uvicorn --reload app.api:api
