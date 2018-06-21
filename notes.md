# End to end Django API in Heroku Notes

0. Install Heroku CLI and do a heroku login

1. Make virtual environment
- .envcr
- direnv allow
- pip install pipenv
2. Install dependencies (that we know we will need)
- Django
- DRF
- Djoser
- gunicorn
- psycopg2-binary
- django-heroku
3. Make the basic django app
- django-admin startproject happydeploy .
3.1 Test application works
4. Start git repository
- git init
- add stuff to git ignore
- make initial commit
- send code to github
4.1 Send code to github
- create github repository
- wire up local dir to remote repo
- git push
5. Deploy to Heroku
- heroku create
- confirm with 'git remote-v' you should see origin and heroku
- configure app to work in heroku
  - add "\*" to allowed host in settings.py
  - import django_heroku in settings
- Add Procfile
  - add web worker: 'web: gunicorn happydeploy.wsgi'
- Test app works locally
  - 'heroku local web'
- push to heroku
