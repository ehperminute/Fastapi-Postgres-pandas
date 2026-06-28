#!/bin/bash

docker compose up -d
until pg_isready -h localhost -p 5432 -U user
do
    echo "Waiting for PostgreSQL..."
    sleep 1
done
python init_db.py

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
