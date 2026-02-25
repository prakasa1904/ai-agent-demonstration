init:
	@(	\
		echo "initialize ai-agent ecosystem..."; \
		python -m venv venv; \
		source venv/bin/activate; \
		pip install -r requirements.txt; \
		make freeze; \
	)

freeze:
	@( \
		source venv/bin/activate; \
		pip freeze > requirements.txt; \
	)

run:
	@( \
		source venv/bin/activate; \
		python src/main.py; \
	)