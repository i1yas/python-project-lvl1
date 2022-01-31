install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
	
build:
	poetry build
	
publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd
