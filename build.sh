#!/usr/bin/env bash

pip install -r requirements.txt

cd backend

playwright install chromium

python manage.py collectstatic --noinput

python manage.py migrate