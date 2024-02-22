#!/bin/sh
python manage.py makemigrations travel_club
python manage.py migrate
echo 'Migrated'