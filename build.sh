#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python indata_project/manage.py collectstatic --no-input
python indata_project/manage.py migrate
