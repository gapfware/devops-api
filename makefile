prod:
	docker compose --env-file .env.prod build

dev:
	docker compose --env-file .env build

run:
	docker compose up -d