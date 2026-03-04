# reMEmber
### A War Diary Platform

**reMEmber** is a digital war diary platform where memories are preserved, shared, and truly felt — not imagined.

It allows users to write privately for themselves or publish publicly for everyone.
The platform gives both military personnel and civilians — including witnesses and those directly affected by war — a space to share their lived experiences, preserve their memories, and speak about realities that must not be silenced.

---

## 🌍 Mission

- Preserve truth
- Give voice to those who cannot be silenced
- Transform personal memories into collective awareness

---

## ✨ Key Features

| Feature | Description |
|----------|------------|
| 📰 Public Feed | View posts shared by users and like publications |
| ✍️ Personal Diary | Create, edit, and manage your own entries |
| 🎵 Music-Associated Memories | Attach a song to reflect the mood of your event |
| 🔍 Search | Search for events and posts |
| 🔥 Top Event | Most liked post is highlighted as the main event |
| 💬 Quote of the Day | Daily meaningful quote |
| 📊 Mood Statistics | Track emotional patterns across posts |
| 🎶 Songs Library | List of songs used in posts |
| 👤 User Profile | Personal profile that you can edit and add photo |
| 🧭 7 Navigation Pages | Structured menu for easy navigation |

---

## 🛠️ Tech Stack

| Layer | Technologies |
|--------|--------------|
| Backend | Python, Django |
| Frontend | HTML, CSS, Django Templates |
| Database | SQLite3 |
| Architecture | 3-Layer Architecture |

---

## 🏗️ Architecture Overview

The project follows a classic 3-layer architecture:

```
User
   ↓
Presentation Layer (UI & Templates)
   ↓
Application Layer (Django Server)
   ↓
Database Layer (SQLite3)
```

### 🔹 Presentation Layer
- Feed of publications
- Authentication (Login / Register)
- Profile page
- Post creation & editing
- Statistics page
- Music page
- Search page

### 🔹 Application Layer
- Business logic
- Authentication & validation
- Post creation & editing
- Like system
- Search & filtering
- Mood statistics calculation
- Top event detection

### 🔹 Database Layer
- Data storage
- ORM queries
- Relationships & indexing

---

## 📁 Project Structure

```
reMEmber/
│
├── diary/                     # Main diary application
│   ├── migrations/            # Database migrations
│   ├── __init__.py
│   ├── admin.py               # Django admin configuration
│   ├── apps.py                # App configuration
│   ├── forms.py               # Forms for creating/editing posts
│   ├── models.py              # Database models
│   ├── tests.py               # Unit tests
│   ├── urls.py                # App routes
│   └── views.py               # Business logic
│
├── reMEmber/                  # Project configuration
│   ├── settings.py            # Global settings
│   ├── urls.py                # Root URLs
│   ├── asgi.py
│   └── wsgi.py
│
├── static/                    # Static files
│   ├── images/
│   └── styles/
│
├── templates/                 # HTML templates
│   ├── diary/
│   ├── users/
│   ├── base.html
│   └── base_app.html
│
├── users/                     # Authentication app
│
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django CLI
└── requirements.txt           # Dependencies
```

---

## 🚀 Setup & Installation

### Prerequisites

- Python 3.10+
- pip
- Virtual environment (recommended)

---

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/reMEmber.git
cd reMEmber
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

MacOS / Linux:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Run Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🎯 Target Audience

- Soldiers and people who have faced war documenting frontline experiences
- Civilians who want to understand real wartime reality
- Anyone who believes memories must not be silenced

---


Some realities cannot be silenced.
Some memories must be preserved.

**reMEmber exists so that truth lives on.**
