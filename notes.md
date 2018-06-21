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
