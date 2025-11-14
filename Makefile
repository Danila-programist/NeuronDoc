HELP_FUN = \
	%help; while(<>){push@{$$help{$$2//'options'}},[$$1,$$3] \
	if/^([\w-_]+)\s*:.*\#\#(?:@(\w+))?\s(.*)$$/}; \
	print"$$_:\n", map"  $$_->[0]".(" "x(20-length($$_->[0])))."$$_->[1]\n",\
	@{$$help{$$_}},"\n" for keys %help;

args := $(wordlist 2, 100, $(MAKECMDGOALS))
ifndef args
MESSAGE = "No such command. Use 'make help' for list of commands."
else
MESSAGE = "Done"
endif

include .env
export

backend_env:  ##@Environment Activate Poetry shell for backend
	cd backend && poetry shell

poetry_install:  ##@Environment Activate install dependencies
	cd backend && poetry install

env_file:  ##@Environment Create or update .env file
	bash bash_scripts/create_or_update_env.sh

test_backend: ##@Testing Run tests for backend
	docker-compose run --rm backend_tests 

run_app:  ##@Docker Start docker-compose services for application
	docker-compose up -d backend_app backend_db

rebuild_run_app:  ##@Docker Rebuild and restart all services for application
	docker-compose up -d backend_app backend_db --build

up:  ##@Docker Start docker-compose all services
	docker-compose up -d  

down:  ##@Docker Stop docker-compose services
	docker-compose down

logs:  ##@Docker Show logs from docker-compose
	docker-compose logs -f

rebuild: ##@Docker Rebuild and restart all services
	docker-compose down && docker-compose up -d --build

psql:  ##@Database Open PostgreSQL inside docker container
	docker exec -it $(DB_CONTAINER_NAME) psql -d $(DB_NAME) -U $(DB_USER)

format:   ##@Code Format code with black for backend
	cd backend && poetry run black .

lint: ##@Code Lint code with pylint for backend
	cd backend && poetry run pylint main.py app tests

clean: ##@Code Remove Python cache files and directories
	bash bash_scripts/clean_files_and_dirs.sh

help: ##@Help Show this help 
	@echo -e "Usage: make [target] ...\n"
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

%::
	@echo $(MESSAGE)

PHONY: backend_env poetry_install env_file up down logs help test_backend rebuild format lint clean