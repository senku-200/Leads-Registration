# Leads Form Django Project

Welcome to the Leads Form Django project! This project is designed to manage leads through a web-based form interface.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Configuration](#configuration)
- [Deployment](#deployment)


## Introduction

The Leads Form Django project

## Prerequisites
Python Installation:
   - Ensure Python is installed on your system. You can download Python from the official website python.org.
   - It's recommended to use Python 3.x (e.g., Python 3.8, Python 3.9) as Python 2.x is no longer supported.

## Installation

To run this project locally or in production, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/senku-200/Leads-Registration.git
   cd Leads-Registration

2. **Create a virtual environment:**
  
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies:**
   
   ```bash
    pip install -r requirements.txt
  
4. **Apply database migrations:**
   
   ```bash
   python manage.py migrate
   
5. **Create a superuser (admin):**
   
   ```bash
   python manage.py createsuperuser
   
6. **Run the development server:**
    
   ```bash
   python manage.py runserver
7. **Access the application at http://localhost:8000 in your web browser.**


## Configuration

Environment Variables

The following environment variables should be set:

- SECRET_KEY: Django secret key for security.
- DEBUG: Set to False in production.
- DATABASE_URL: URL of the production database (e.g., PostgreSQL).
- ALLOWED_HOSTS: List of allowed hostnames for the production environment.

## Settings

Adjust Django settings in leads_form/settings.py as needed, especially for production deployment (e.g., STATIC_ROOT, MEDIA_URL, SECURE_SSL_REDIRECT).

##Deployment

For deploying this project to production, follow these general steps:

- Set up a production server (e.g., AWS, DigitalOcean).
- Configure a domain name and update DNS settings.
- Install necessary software (Python, web server like Nginx or Apache).
- Secure your server with HTTPS using SSL certificates (e.g., Let's Encrypt).
- Deploy the code using deployment tools like Fabric, Ansible, or Docker.









