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

backend_env:  ##@Environment Activate Poetry shell for backend
	cd backend && poetry shell

poetry_install:  ##@Environment Activate install dependencies
	cd backend && poetry install

env_file:  ##@Environment Create or update .env file
	bash bash_scripts/create_or_update_env.sh

up:  ##@Docker Start docker-compose services
	docker-compose up -d  

down:  ##@Docker Stop docker-compose services
	docker-compose down

logs:  ##@Docker Show logs from docker-compose
	docker-compose logs -f

help: ##@Help Show this help 
	@echo -e "Usage: make [target] ...\n"
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

%::
	@echo $(MESSAGE)

PHONY: backend_env