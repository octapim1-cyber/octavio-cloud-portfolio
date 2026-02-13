# docker-app

Tiny FastAPI demo (placeholder for model). Run locally:

1. Create virtualenv:
	python3 -m venv .venv
	source .venv/bin/activate
2. Install:
	pip install -r requirements.txt
3. Run:
	uvicorn main:app --reload --port 8000

Test:
curl http://127.0.0.1:8000/health
