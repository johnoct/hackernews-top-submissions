import requests
import json
import flask
from multiprocessing.dummy import Pool as ThreadPool
from operator import itemgetter
from flask import Flask
app = Flask(__name__)


@app.route('/top_hn_subs')
def hn_submissions():
    # Make an API call and store the response.
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url)

    # Process information about each submission.
    submission_ids = r.json()
    submission_dicts = []
    pool = ThreadPool(12) 

    # function
    def get_submission(submission_id):
        # Make a seperate API call for each submission.
        url = ('https://hacker-news.firebaseio.com/v0/item/' +
               str(submission_id) + '.json')
        submission_r = requests.get(url)
        response_dict = submission_r.json()

        submission_dict = {
            'title': response_dict['title'],
            'link': 'https://news.ycombinator.com/item?id=' + str(submission_id),
            'comments': response_dict.get('descendants', 0),
        }
        submission_dicts.append(submission_dict)
    pool.map(get_submission, submission_ids[:15])

    submission_dicts = sorted(
        submission_dicts, key=itemgetter('comments'), reverse=True)

    return flask.jsonify(submission_dicts)
