VENV=.venv

help:
	@echo "install        - install dependencies"
	@echo "test           - run tests"
	@echo "lint           - lint bash scripts"
	@echo "run            - run app locally"
	@echo "docker-build   - build docker image"
	@echo "docker-run     - run docker container"
	@echo "compose-up     - start docker compose"
	@echo "compose-down   - stop docker compose"
	@echo "server-info    - show server info"
	@echo "ansible-run    - run ansible playbook"
	@echo "ansible-check  - run ansible check"
	@echo "ansible-dry    - run ansible changes"


install:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r app/requirements.txt

run:
	$(VENV)/bin/python app/main.py

test:
	PYTHONPATH=. .venv/bin/pytest app/tests/

lint:
	shellcheck scripts/*.sh

docker-build:
	docker build -t simple-app .

docker-run:
	docker run -p 5000:5000 simple-app

compose-up:
	docker compose up -d

compose-down:
	docker compose down

server-info:
	./scripts/server-info.sh http://localhost:5000/health

ansible-run:
	ansible-playbook -i ansible/inventory.ini ansible/playbook.yml

ansible-check:
	ansible-playbook --syntax-check -i ansible/inventory.ini ansible/playbook.yml

ansible-dry:
	ansible-playbook -i ansible/inventory.ini ansible/playbook.yml --check
