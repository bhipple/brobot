.PHONY: all lint test

all: lint test format

lint:
	pyflakes *.py
	pep8 *.py

format:
	yapf -ir .

test:
	python test_brobot.py
