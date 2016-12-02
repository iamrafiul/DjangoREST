# RESTful API using Django Rest Framework

## Introduction
A simple RESTful API built in [Django Rest Framework(DRF)](http://www.django-rest-framework.org/) using Django DB Models and DRF's Model View Set.

A sqlite3 database named "student.sqlite3" is included in the repository with some sample data for testing.

## Running the app
From the root directory run the following commands in terminal

```
pip install -r requirements.txt

python manage.py runserver
```
It will run the server at localhost:8000/ by default.



### Note
If the first 'pip' command doesn't work, you can install django and django-rest-framework using the following command.

```
pip install django djangorestframework
```

If pip can't install the packages due to access denied issue, try with sudo and it's always better to run the project from virtual environment.
