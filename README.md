# Semnan University Programming Competition Platform

Backend service for the programming competition platform of Semnan University, developed using Django and Django REST Framework.

## Overview

This project provides the backend infrastructure for managing and presenting programming competitions and their related content.

The system exposes RESTful APIs for retrieving competition information, articles, media content, winning teams, FAQs, and other competition-related data.

## Features

* Programming competition management
* Competition details and metadata
* Competition articles
* Winning team management
* Competition images and videos
* Competition reports and scoreboards
* FAQ management
* RESTful APIs
* Media file management
* PostgreSQL database
* Separate development and production settings

## API

The backend provides RESTful endpoints for accessing competition and article data.

### Competition

The API supports:

* Listing competitions
* Retrieving competition details by slug
* Competition-related media
* Winning teams
* FAQs
* Competition reports and scoreboards

### Articles

The API supports:

* Listing articles
* Retrieving article details by slug
* Article media

## Tech Stack

* **Python**
* **Django**
* **Django REST Framework**
* **PostgreSQL**

## Project Structure

```text
Semantic/
├── Semantic/
│   ├── settings/
│   │   ├── common.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── competition/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── registeration/
├── manage.py
└── README.md
```

## Database

PostgreSQL is used as the primary relational database.

The project uses Django's ORM for database modeling and querying.

## Development

Clone the repository:

```bash
git clone https://github.com/AMahdi8/Semantic.git
cd Semantic
```

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install the project dependencies according to the project's dependency configuration.

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## Project Type

**University Final Project**

Developed as the backend of a programming competition platform for Semnan University.
