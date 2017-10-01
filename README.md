# To do List
This project consists of a list of tasks,
in which a specific user can load independent tasks.

It has a registration and login system.

The actions allowed on the tasks are, create, edit and mark as it turns out.

Each task consists of date of creation and expiration, title, description
and the possibility of attaching a file.

### Technologies

Backend technologies:

* [Python]
* [Django]

Style Tools:

* [Md-Bootstrap]
* [Bootstrap]

Complementary tools for js:

* [Jquery] - use bootstrap

## First steps:

#### 1. [Install python2.7](https://www.python.org/download/releases/2.7/)

#### 2: Configure virtual environment within the whole project. Choose between [virtualenv](https://virtualenv.pypa.io/en/stable/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

#### 3: Enable virtual environment

#### 4: Located within the folder /todo

#### 5: Install dependencies for backend:
        pip install -r requirements.txt

#### 6: Running django migrations:
        python manage.py migrate

#### 7: Running backend server:
        python manage runserver

#### 8: Open Browser on [localhost](http://127.0.0.1:8000)
