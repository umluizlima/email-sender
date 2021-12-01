.PHONY: environment
environment:
	pyenv install -s 3.10.0
	pyenv uninstall --force email-sender
	pyenv virtualenv 3.10.0 --force email-sender
	pyenv local email-sender

.PHONY: install
install:
	pip freeze | xargs -r pip uninstall -y && \
	pip install -r requirements-dev.txt && \
	pre-commit install

.PHONY: broker_init
broker_init:
	docker-compose up -d broker

.PHONY: test
test:
	PYTHONPATH=. \
	python -m pytest --cov=app -s

.PHONY: run_worker
run_worker: broker_init
	celery -A app.worker worker --loglevel debug

.PHONY: run_api
run_api: broker_init
	uvicorn --reload app.api:api

.PHONY: run
run:
	make -j run_worker run_api
