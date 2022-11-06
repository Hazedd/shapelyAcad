install:
	python -m pip install --upgrade pip
	pip install flit
	flit install --deps develop

test:
	mpytest --cov=shapelyAcad/ --cov-report=term-missing --cov-fail-under=85

lint:
	flake8 ./shapelyAcad ./tests

typecheck:
	mypy shapelyAcad/ --show-traceback

format-check: isort-src-check
	black --check .

format: isort-src
	black .

isort-src-check:
	isort --check-only ./shapelyAcad ./tests

isort-src:
	isort ./shapelyAcad ./tests

bumpversion-release:
	bumpversion release

bumpversion-major:
	bumpversion major

bumpversion-minor:
	bumpversion minor

bumpversion-patch:
	bumpversion patch

bumpversion-build:
	bumpversion build

build-wheel:
	flit build

check-all:
	make test
# 	make typecheck
	make format
	make lint
# 	mkdocs build
