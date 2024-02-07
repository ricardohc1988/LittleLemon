# Meta Capstone Project

This repository contains the Capstone Project for the Meta course on Coursera.

## Overview

The project is a simple Django application for managing a restaurant's menu and bookings. It includes basic functionalities such as creating and viewing menu items, as well as handling reservations.

## Tech Stack:

* **Django**: Web framework for backend development.
* **Django REST Framework**: API development framework built on top of Django.
* **Pipenv**: Virtual environment management tool.
* **Djoser**: Django REST Framework extension for user authentication.

## Setup:

1. Clone this repository.
2. Create a virtual environment and install required dependencies using pipenv install
3. Activate the virtual environment using pipenv shell
4. Apply database migrations: python manage.py migrate
5. Create a superuser: python manage.py createsuperuser
6. Run the development server: python manage.py runserver

## API Endpoints

### Menu Items:
* List all: /api/menu/ (GET)
* Retrieve details: /api/menu/<int:pk>/ (GET)
* Create new: /api/menu/ (POST)
* Update existing: /api/menu/<int:pk>/ (PUT or PATCH)
* Delete: /api/menu/<int:pk>/ (DELETE)
### Bookings:
* List all: /api/booking/ (GET)
* Retrieve details: /api/booking/<int:pk>/ (GET)
* Create new: /api/booking/ (POST)
* Update existing: /api/booking/<int:pk>/ (PUT or PATCH)
* Delete: /api/booking/<int:pk>/ (DELETE)
### Authentication:
* Obtain authentication token: /api/auth/token/login/ (POST)
