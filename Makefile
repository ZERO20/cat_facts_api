build:
	docker-compose -f docker-compose.yml build

build-no-cache:
	docker-compose -f docker-compose.yml build --no-cache

start:
	docker-compose -f docker-compose.yml up -d

stop:
	docker-compose -f docker-compose.yml stop

rebuild:
	docker-compose -f docker-compose.yml up -d --build
