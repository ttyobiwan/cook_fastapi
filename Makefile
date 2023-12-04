SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

.DEFAULT_GOAL := help
.PHONY: help
help: ## Display this help section
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z\$$/]+.*:.*?##\s/ {printf "\033[36m%-38s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: up
up: ## Start docker containers
	docker compose up

.PHONY: build
build: ## Build docker images
	docker compose build

.PHONY: enter
enter: ## Enter backend container
	docker compose exec fastapi bash

.PHONY: install
install: ## Install all Python dependencies
	pip install -r requirements/dev.txt

.PHONY: test
test: ## Run tests
	pytest

.PHONY: lint
lint: ## Run linters
	pre-commit run --all-files
