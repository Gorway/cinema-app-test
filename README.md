📽️ Cinema Booking — Test Task (Backend, Django)
A simple cinema seat booking application built with Django and Django REST Framework.

✅ Features

🎬 Create multiple rooms (e.g. Ani, Van, Dvin)

🍿 Schedule multiple movies per room (Alabalanica, Mer Bak 4, Big story in little town)

🪑 View and book seats for each screening (10 rows × 8 seats)

🚫 Booked seats are unavailable until the screening ends

🛠 Admin panel for full CRUD on rooms, movies, screenings

📄 CSRF-protected API for secure booking via frontend

📦 Requirements
Python 3.10

SQLite (default)

Django >= 4.2

djangorestframework >= 3.14

🚀 Setup
Clone the repository (or copy files into your project folder)

Create virtual environment:

    python3.10 -m venv venv
    source venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

The project includes a pre-filled `db.sqlite3` with:

- Rooms: Ani, Van, Dvin
- Movies and Screenings
- 10×8 seat grid per room

👉 **No need to run migrations or populate data manually.** Just start the server and everything is ready.

If you do want to reset or change the DB structure:

    python manage.py makemigrations
    python manage.py migrate

Create superuser (for admin panel):

    python manage.py createsuperuser

Run development server:

    python manage.py runserver

Open in browser:

    Frontend UI: http://127.0.0.1:8000/

    Admin panel: http://127.0.0.1:8000/admin/


📁 Tech Stack
Django 4.2+

Django REST Framework

SQLite

Vanilla JS frontend (included in templates/index.html)

📌 Note
No JavaScript framework used — pure Django + HTML/JS for simplicity and clarity.
Code formatted with black