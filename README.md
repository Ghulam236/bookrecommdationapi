first goto google cloud console and create project after this enable the book api
 and then create credential to get API Key copy that api and use in your project
step1- (a) create folder BookRecoomendation
       (b) create virtual environment
                  virtualenv xenv # comand to create virtual environment xenv is name of virtualenv
        (c)  activate virtual environment
                source xenv/bin/activate
step2- (a) install django
             pip install django
        (b) install django rest framework
             pip install djangorestframework
        (c) install requests for get data from google api
step 3- (a) create project
               django-admin startproject bookrecommendation
        (b) go to project directory
             cd bookrecommendation
step 4- (a) create app inside project menas current directory
             python manage.py startapp book # app name is book
step 5 (a) add app book in settings.py inside installed
             'book'
        (b) add rest framework also inside installed
             'rest_framework
step 6 (a) create class in views.py
            BookSearchView() # this class serach the data according to query parameter
        (b) create utils.py inside book app to get data from google api

        (c) create logic to fetch and filter data
step 7 (a)create urls for serch in urls.py

step 8- (a) create templates inside this create book_dashboard.html to show the data to user

step 9    (a) for crud create class in models.py for book recommendation
          (b) create serializers.py in book app to handle complex data
          (c) python manage.py makemigrations # to convert class fileds int sql
          (d) python manage.py migrate   # to ceate table
step 10 (a) create class in views api crud use modelviewset and handle crud operations
        (b) also handle filtering and sorting inside class api modelviewset

Request and Response 
        Request and Response should be in json format
Base_url: http://127.0.0.1:8000/
endpoint:search+query