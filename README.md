# Insta-pic

## Author
https://github.com/brenda-wanjiku/instagram

## Description
A clone of the photo-app, Instagram.

## How to use 

1. First, for new users they have to register and login to access the application,
2. On login, the user will see the  posts by other account holders and can comment on them. 
3. On clicking an image a user can see it's details such as comments and number of likes. The user can also like or unlike image from this page.
4. A user can upload pictures from your profile
5. The user can view their profile by cliking on the profile option on the navbar. The user can edit once on the profile page
6. The user can search for a user through the search form on the navbar.
7. To access admin page use the following credentials: Username: brendawanjiku29, password: brenda29

## Technolgies used
1. HTML and CSS
2. Python
3. Django
4. Postgres
5. Heroku
6. Git and GitHub

## Set up and Installation
### Prerequisites
* python3.8
* pip
* Virtual environment(virtualenv)
* Django 
* PostgreSQL
* Heroku
* Pillow==7.1.2

The user will require git, django, postgres and python3.8 installed in their machine. To install these two, you can use the following commands

1. git
```$ sudo apt install git-all```

2. python3.8
```$ sudo apt-get install python3.8.```

3. django
``` pip install django```

4. postgres
```$ sudo apt-get install postgresql postgresql-contrib```

5. django-bootstrap4
```pip install django-bootstrap4```


### Installation
1. To access this application on your command line, you need to clone it 
`https://github.com/brenda-wanjiku/instagram.git`
2. You can then run the server with:
`python3.6 manage.py runserver`
3. You can make changes to the db with
`python3.6 manage.py makemigrations insta`
`python3.6 manage.py migrate`
4. You can run tests:
`python3.6 manage.py test insta`


### Creating the virtual environment
* Use the following commands in your terminal to create virtual environment

    $ python3.8 -m venv --without-pip virtual

    $ source virtual/bin/env

    $ curl https://bootstrap.pypa.io/get-pip.py | python
    



# Live Site
* Can be accessed here https://brenda-instagram.herokuapp.com/

* To log in as an admin you can use the following credentials:
      username : brendawanjiku29 and password: brenda29


# Author's Contact
If you need any clarifications or have feedback on this project , contact the author at brendawanjiku@gmail.com

# License
This software is Licensed under MIT license Copyright (2020)
https://raw.githubusercontent.com/brenda-wanjiku/instagram/master/LICENSE
