#!/bin/bash
pip install -r requirements.txt
docker compose up -d

python init_db.py

python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
