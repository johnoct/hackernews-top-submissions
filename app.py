import requests
import json
import flask
from flask_cors import CORS
from concurrent.futures import ProcessPoolExecutor
from requests import Session
from requests_futures.sessions import FuturesSession
from operator import itemgetter
from flask import Flask
app = Flask(__name__)
CORS(app)

@app.route('/top_hn_subs')
def hn_submissions():
    
    session = FuturesSession(executor=ProcessPoolExecutor(max_workers=10),
                         session=Session())

    # Make an API call and store the response.
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url)

    
    # Process information about each submission.
    submission_ids = r.json()
    submission_dicts = []

    # Craft an array of URLS
    urls = []
    for submission in submission_ids[:15]:
        urls.append('https://hacker-news.firebaseio.com/v0/item/{}.json'.format(submission))

    sessions = []
    for url in urls:
        sessions.append(session.get(url))

    responses = []
    for session in sessions:
        responses.append(session.result())      

    for r in responses:
        response_dict = r.json()
        submission_dict = {
            'title': response_dict.get('title', ''),
            'link': 'https://news.ycombinator.com/item?id={}'.format(response_dict.get('id', 0)),
            'comments': response_dict.get('descendants', 0),
            'score': response_dict.get('score', 0),
        }
        submission_dicts.append(submission_dict)

    submission_dicts = sorted(
        submission_dicts, key=itemgetter('score'), reverse=True)
    
    data_dict = {}
    data_dict['data'] = submission_dicts

    return flask.jsonify(data_dict)
