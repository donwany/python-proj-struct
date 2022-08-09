install:
	pip install --upgrade pip && pip install -r requirements.txt
format:
	black main.py
run:
	python main.py
build:
	docker build -t worldbosskafka/<repo-name> .
push:
	docker push worldbosskafka/<repo-name>
lint:
	pytest main.py
test:
	python -m pytest -vv --cov=main.py tests/test_*.py
dist:
	python setup.py sdist bdist_wheel
pypi:
	twine upload --repository pypi dist/*
deploy:
	echo "deploy command goes here"
clean:
	rm -rf dist
all:
	install format run test lint dist
