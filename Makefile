
.PHONY: start build test

start:
	docker compose up -d

build:
	docker compose build

run:
	python backend/main.py

test:
	cd backend && pytest
