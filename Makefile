test:
	@coverage run -m pytest tests/test_*.py
	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"
