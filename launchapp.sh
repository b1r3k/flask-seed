#!/bin/bash

if [ "$CONFIG" == "Dev" ]
then
    python flaskApp/main.py
else
    gunicorn flaskApp.main:app -w 3
fi