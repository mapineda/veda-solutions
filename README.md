# Veda Solutions 

## About

Simple MLB stats scraper that takes pandas dataframe and converts to json file
The data in the .json file is then wrapped in an object-array and then served 
locally on port: 5000 

## Pre-requisites:
- Docker

## How to:

### Set up:
- in root `mlb-app` build docker container
`docker-compose -f local.yml build`

### Run:

- run the stack `docker-compose -f local.yml up`


### Create a User

1. run migrations
`docker-compose -f local.yml run --rm django python manage.py migrate`
2. run create superuser command
`docker-compose -f local.yml run --rm django python manage.py createsuperuser`
3. navigate to `http://0.0.0.0:8025/` to confirm email


## Methodology:

This application was created using cookie-cutter django for quick setup of a 
production-ready django project.

## Structure:
mlb-app uses a task management system (celery) to scrape data that will be
saved in our database (postgres). This data is then serialized and served over api
endpoints.
