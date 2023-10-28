# Todo API Project

A simple Flask-based Todo APIs project that allows you to create, read, update, and delete tasks.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)


## Overview
This project provides a RESTful API for managing tasks in a todo list. It includes basic CRUD functionality, allowing you to create, retrieve, update, and delete tasks. 

## Features
- Create tasks
- Retrieve tasks
- Update tasks
- Delete tasks

## Prerequisites
- Python 3.7+
- Flask (automatically installed via `requirements.txt`)

## Installation
1. # Clone the repository:
   git clone https://github.com/Alija69/todo.git
   cd todo

2. # Create virtual environment
     python -m venv venv
   # On Windows:
    venv\Scripts\activate
   # On macOS and Linux:
    source venv/bin/activate
   
3. # Install requirements
    pip install -r requirements.txt

4. # Create .env file and set environment variables as .env.example file
   
5. # create .flaskenv and add assign value as below
     FLASK_APP=main.py
     FLASK_DEBUG = false
     FLASK_RUN_PORT = 8080
   
## Now run command flask run to start your app
   


