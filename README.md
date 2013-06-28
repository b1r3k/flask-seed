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

Foreman takes variables from .env and creates environment variables.
Config.settings defines defaults and overrides them with environment variables, eg. for dev setup use FLASK_ENV=development and DEBUG=True
Variables should have all uppercase names!
.env file should not go to production or should be ignored on production setup