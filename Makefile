.PHONY: all lint test

all: lint test

lint:
	pyflakes *.py
	pep8 *.py

test:
	python test_brobot.py
