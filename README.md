<!-- Please update value in the {}  -->

<h1 align="center">Django Blog App</h1>


<div align="center">
  <h3>
    <a href="http://mskose.pythonanywhere.com/">
      Demo
    </a>
     | 
    <a href="https://github.com/MSKose/django-blog-app">
      Project
    </a>
 
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Overview](#overview)
- [Stack & Tools](#stack)
- [Project Structure](#project-structure)
- [How to use](#how-to-use)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview

This is my first Full-Stack project where I did both the Back-End and the Front-End. Along the way, I got familiarized with the Django Framework. Notions I have learned include authentication, database relations, Class based views and Function based views, Django Template language, and HTMX. 

![screenshot](https://user-images.githubusercontent.com/16707738/92399059-5716eb00-f132-11ea-8b14-bcacdc8ec97b.png)

<h2 id="stack">Stack & Tools</h2>

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- Django
- Bootstrap
- HTML
- CSS
- HTMX
- JavaScript

## Project Structure

```bash
.──── django-blog-app (repo)
│
├─── README.md
├── blog
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── static
│   │   └── blog
│   │       ├── css
│   │       │   └── main.css
│   │       ├── images
│   │       │   ├── bg.jpeg
│   │       │   └── favicon.png
│   │       └── js
│   │           └── main.js
│   ├── templates
│   │   └── blog
│   │       ├── about.html
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── likes_area.html
│   │       ├── post_comment.html
│   │       ├── post_confirm_delete.html
│   │       ├── post_detail.html
│   │       └── post_form.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── main
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media
│   ├── blog_default.jpg
│   ├── blog_pics
│   │   └── javascript.png
│   ├── default.jpg
│   └── profile_pics
│       └── profile_pic.jpg
├── requirements.txt
└── users
    ├── __init__.py
    ├── __pycache__
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    ├── models.py
    ├── signals.py
    ├── templates
    │   └── users
    │       ├── login.html
    │       ├── logout.html
    │       ├── profile.html
    │       └── register.html
    ├── tests.py
    ├── urls.py
    └── views.py

```

## How To Use 

To clone and run this application, you'll need [Git](https://git-scm.com)

```bash
# Clone this repository
$ git clone https://github.com/MSKose/django-blog-app

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt

# Add .env file
    add your SECRET_KEY in a .env file

# Run the app
    $ python manage.py runserver
```

## Contact

- [GitHub](https://github.com/MSKose)
- [Linkedin](https://www.linkedin.com/in/mustafa-kose-linked/)