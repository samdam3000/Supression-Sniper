#!/bin/bash

# Install dependencies (optional safety)
pip install -r requirements.txt

# Start the app using gunicorn on localhost:8000
gunicorn app:app --bind 0.0.0.0:8000