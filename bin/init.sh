#!/bin/bash

psql < bin/init-db.sql
pipenv install --dev
pipenv run python bin/populate-regions.py
pipenv run python bin/populate-points.py