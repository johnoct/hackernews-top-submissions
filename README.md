# hackernews-top-submissions
Get the top hacker news submissions.

```
pip install -r requirements.txt
FLASK_APP=app.py flask run
```

heroku deploy
```
heroku login
```
create `Procfile`
```
web: gunicorn app:app --log-file=-
```
heroku crate app
```
heroku create
```
push code to heroku
```
git push heroku master
```
[Top 15 Hacker News](https://young-retreat-74774.herokuapp.com/top_hn_subs)
