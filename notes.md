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
- Commit all heroku stuff
- Push code to heroku to initiate deploy
 - 'git push heroku master'
6. Start Application
- 'python manage.py startapp <appname>'
7. Add Template View in 'views.py'
- Call it IndexView, configure class to use template
- Create template directory in 'app' dir
- Create index.html
8. Wire up my view to the '/' route in 'urls.py'
- test route works in brower
- When it doesn't work, make sure you added your app to 'installed apps'
9. Deploy to Heroku
- git commit
10. Create custom User model in our 'app/models.py'
- https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#substituting-a-custom-user-model
- add "AUTH_USER_MODEL" attribute to settings.py
11. Add rest_framework and rest_framework.authtoken to installed apps
12. makemigrations and migrate
- locally - python manage.py migrate
- on heroku (git push all migrations and user model stuff first)
 - 'heroku run python manage.py migrate'
13. Implement user login / logout (djoser)
http://djoser.readthedocs.io/en/stable/authentication_backends.html#token-based-authentication
- add djoser to installed apps
- add paths to urls - import include
- run 'python manage.py createsuperuser' to create superuser in app
- Test user token creation works
 - post to '/auth/token/create' with Username and Password in request body
- Test user token destroy works (Postman)
 - Post to '/auth/token/destroy' with auth token as header (nothing in body):
 Authorization Token <paste here>
 - WOOPS we didn't tell settings to use it to use Token Authentication paste into settings:
 REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}
- Now it should work
14. Commit all changes - push to Heroku
- create super user in Heroku
- 'heroku run python manage.py createsuperuser'
- test auth token create and destroy but with heroku post as url
15. add timestamp model to app
- makemigrations and migrate locally
16. Heroku deploy git add . git commit - git push heroku master
17. Migrate new model on heroku
18. Create List and Creat API View for timestamp model
- create serializer for Timestamp model (serializers.py)
- add queryset and serializer_class to API View
19. Add a path for Timestamp API View in urls.py
- path('timestamps/', TimestampListCreateAPIView.as_view())
20. (Double check for any typos or import errors)
21. Test locally that you can GET to '/timestamps/' and POST to create a '/timestamps/'
22. 
