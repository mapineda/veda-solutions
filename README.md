# Veda Solutions 

## About

Simple MLB stats scraper that takes pandas dataframe and converts to json file
The data in the .json file is then wrapped in an object-array and then served 
locally on port: 5000 

## Pre-requisites:
- virtualenv

## How to:

### Set up:
1. create virtual env
2. install requirements by running `pip install -r requirements.txt`

### Run:
1. To get flask api running 
`export FLASK_APP=app.py`
`python -m flask run`
