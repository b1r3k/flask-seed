# flask-seed

Skeleton for flask based web applications.

## Features
* integrated blueprint
* config with production / development environment management
* template for e2e & unittest tests
* ready configuration files for launching via:
    - FastCGI
    - gunicorn

## Dependencies
* foreman
* gunicorn (optional)
* flask-restful (req. by REST API blueprint)
* flup (optional, req. by Fast-CGI, eg. bluehost shared hosting)

## Usage

1. Clone
2. install virtual env
3. pip install -r requirements.txt
4. foreman start

## Adjusting development environment

1. config/config.py defines different config objects default containging settings for the app.
    - for development environment use config.Dev object
1. If you want to select config setup, without code modification you can set CONFIG variable with class name defined in config/config.py
1. Config object can be overriden by specifing path to config via environmental variable FLASK_SEED_CONFIG
    - Foreman can do this job, just set the variable in the .env file