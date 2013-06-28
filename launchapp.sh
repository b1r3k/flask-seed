#!/bin/bash

if [ "$FLASK_ENV" == "development" ]
then
    python flaskApp/main.py
else
    gunicorn flaskApp.main:app -w 3
fi