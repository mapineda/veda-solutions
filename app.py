import os
import json
from flask import Flask

app = Flask(__name__)

# get all stats from json file
@app.route('/', methods=['GET'])
def index():
    filename = os.path.join('', 'mlb_stats.json')
    with open(filename) as stats_file:
        data = json.load(stats_file)
        return data 