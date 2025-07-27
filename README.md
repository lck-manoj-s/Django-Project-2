# Try QTech

## Table of Contents
- [Overview](#overview)
- [Technology Stack](#technology-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)

## Overview
Try QTech is a techical quiz platform hosted online through websites where people can solve through technical question in an interactive way. 

## Technology Stack
### 1. 💻 Frontend
- **HTML** – Core language that builds the skeleton of the website.

- **CSS3** – Style sheet that styles the website.

- **JavaScript (ES6+)** – Core scripting language.

### 2. 🌐 Backend
- **Django** – Python web framework with wide array of built-in tools and components for common web development tasks.
  

### 3. 🛢️ Database
- **MySQL** – SQL database to store all the data in a tabular form.

- **Django ORM** – ORM to define schemas and interact with MySQL easily.

## Features
- Customizable number of question for each quiz

- Personalized completion rewards to keep exploring other quizzes

- Smooth transistion & animation for navigation between questions

- Get an expirement before attending actual quiz
  
## Project Structure
```
webquiz/
├── main/
|   ├── apps.py
|   ├── models.py
│   ├── urls.py
│   ├── templates/
│   │   ├── demo.html
│   │   ├── details.html
│   │   ├── results.html
│   │   ├── home.html
│   │   └── quiz.html
│   └── views.py
├── webquiz/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── static/
```
### Backend
- `main/apps.py`: Registers the Django app configuration for the main application.
- `main/models.py`: Defines database models for quizzes, questions, options, and results.
- `main/urls.py`: Declares URL patterns specific to the main app (e.g., /quiz/, /results/).
- `main/views.py`: Contains the core logic for rendering pages, handling submissions, and scoring the quiz.
- `webquiz/asgi.py`: ASGI configuration for asynchronous deployment (e.g., with Daphne or Uvicorn).
- `webquiz/settings.py`: Central configuration file for the Django project, including installed apps, middleware, and database settings.
- `webquiz/urls.py`: Root URL configuration that includes app-specific routes (like main/urls.py).
- `webquiz/wsgi.py`: WSGI configuration for deployment using traditional web servers (e.g., Gunicorn).

### Frontend
- `demo.html`: Template for displaying a demo or preview of the quiz system.
- `details.html`: Template showing quiz or user-specific details.
- `results.html`: Displays the quiz results to the user.
- `home.html`: Landing or home page template of the quiz application.
- `quiz.html`: Renders the quiz questions and captures user responses.
- `static/`: Contains static files like CSS, JS, and images used by the templates.
  
## Installation
### 1. Clone the repository
`git clone https://github.com/yourusername/Try-QTech.git`

### 2. Install Necessary Dependencies
Make sure to have Python installed in the system. After python has been successfully installed, install the dependencies from requirements.txt
```
pip install requirements.txt
```

## Usage
### 1. Start the Django server
```
python manage.py runserver
```
