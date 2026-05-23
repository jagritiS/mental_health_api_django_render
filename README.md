# Mental Health Chatbot API 

A simple Mental Health Support Chatbot API built using Django REST Framework.

This project provides supportive chatbot responses based on mood-related keywords such as stress, sadness, anxiety, and loneliness.

---

# Features

- Mental health chatbot API
- Mood-based supportive responses
- REST API with JSON responses
- Beginner-friendly Django project
- Ready for deployment on Render

---

# Tech Stack

- Python
- Django
- Django REST Framework
- Gunicorn
- PostgreSQL
- Render

---
# API Endpoints

## POST `/api/chat/`

Send a message to the chatbot.

### Request

```json
{
  "message": "I feel stressed"
}
```

### Response

```json
{
  "user_message": "i feel stressed",
  "reply": "Try taking deep breaths and short breaks."
}
```

---

## GET `/api/moods/`

Returns supported moods.

### Response

```json
{
  "supported_moods": [
    "sad",
    "stress",
    "anxious",
    "lonely"
  ]
}
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/jagritiS/mental_health_api_django_render.git
```

```bash
cd mental_health_api_django_render
```

---

# Create Virtual Environment

## Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Migrations

```bash
python manage.py migrate
```

---

# Run Server

```bash
python manage.py runserver
```

Open:

```bash
http://127.0.0.1:8000/api/moods/
```

---

# Deployment on Render 

## STEP 1 — Install Deployment Packages

Run:

```bash
pip install gunicorn whitenoise dj-database-url psycopg2-binary
```


---

# STEP 2 — Create requirements.txt

Run:

```bash
pip freeze > requirements.txt
```

### OUTPUT

```bash
requirements.txt created
```

---

# STEP 3 — Create Procfile

Create file:

```bash
Procfile
```

Add:

```bash
web: gunicorn mentalhealth.wsgi
```

---

# STEP 4 — Create build.sh

Create file:

```bash
build.sh
```

Add:

```bash
#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
```

Make executable:

```bash
chmod +x build.sh
```


# STEP 5 — Update settings.py

Add:

```python
ALLOWED_HOSTS = ['*']
```



# STEP 6 — Push to GitHub

Run:

```bash
git add .
git commit -m "Deployment setup"
git push
```

---

# STEP 7 — Deploy on Render

Open Render

- New Web Service
- Connect GitHub
- Select repository

### Build Command

```bash
./build.sh
```

### Start Command

```bash
gunicorn mentalhealth.wsgi
```

---



# OUTPUT

```bash

https://mental-health-api-django-render.onrender.com/api/moods/
```
---

# Project Structure

```bash
mental_health_api_django_render/
│
├── chatbot/
├── mentalhealth/
├── manage.py
├── requirements.txt
├── Procfile
├── build.sh
└── README.md
```

---

