import requests
import json
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
    for submission_id in submission_ids[:30]:
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

    submission_dicts = sorted(
        submission_dicts, key=itemgetter('comments'), reverse=True)

    return json.dumps(submission_dicts, indent=4)
