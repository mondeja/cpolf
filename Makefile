PHONY: dev-install
dev-install:
	@python3 -m pip install -e .[dev] && clear

PHONY: docs
docs: dev-install
	cd docs && make html && cd ..

PHONY: tests
tests: dev-install
	pytest test -svv

PHONY: lint
lint: dev-install
	flake8 setup.py test docs/conf.py
