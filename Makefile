container_name = wedding-tools-django

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  build                 Build docker image"
	@echo "  up                    Run the docker containers"
	@echo "  down                  Stop the docker containers"
	@echo "  destroy               Stop the docker containers AND kill volumes"
	@echo "  logs           	   View output from docker container"
	@echo "  sh                    Run docker container shell"
	@echo "  shell                 Run Django shell"
	@echo "  makemigrations        Create Django migrations"
	@echo "  migrate               Migrate database"
	@echo "  createsuperuser       Create super user"
	@echo "  tests                 Run tests"
	@echo "  makemessages          Updates locale files"
	@echo "  compilemessages       Compiles locale files"

build:
	docker-compose -f docker-compose.yml build --no-cache

up:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down

destroy:
	docker-compose -f docker-compose.yml down -v

logs:
	docker-compose -f docker-compose.yml logs --tail=100 -f

sh:
	docker exec -ti $(container_name) sh

shell:
	docker exec -ti $(container_name) python manage.py shell

makemigrations:
	docker exec -ti $(container_name) python manage.py makemigrations

migrate:
	docker exec -ti $(container_name) python manage.py migrate

createsuperuser:
	docker exec -ti $(container_name) python manage.py createsuperuser

test:
	docker exec -ti $(container_name) python manage.py test

makemessages:
	docker exec -ti $(container_name) python manage.py makemessages --all

compilemessages:
	docker exec -ti $(container_name) python manage.py compilemessages
