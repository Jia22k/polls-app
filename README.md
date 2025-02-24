# Polls App

A simple **Django-based Polls Application** that allows users to vote on different poll questions. Users must log in to vote, and they can change their vote at any time. Admins can access a dashboard to manage polls.

## Features 🚀
- User authentication (login/logout/register)
- Users can vote on polls (one vote per user, can change vote)
- Admin panel for managing polls and choices
- Pretty UI with a **purple theme** ✨
- Secure API endpoints with CSRF protection

## Setup & Installation 🛠️
### Prerequisites
Ensure you have the following installed:
- Python (3.10 or later)
- Django (5.0.1)
- Git
- Virtual Environment (venv)

### Clone the Repository
```bash
git clone https://github.com/Jia22k/polls-app.git
cd polls-app
```

### Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser (Admin Access)
```bash
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### Run the Development Server
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your browser.

---

## API Endpoints 🖥️
| Endpoint           | Method | Description |
|-------------------|--------|-------------|
| `/`               | GET    | Home page with polls |
| `/<poll_id>/`    | GET    | Poll detail page |
| `/<poll_id>/vote/` | POST   | Submit vote (must be logged in) |
| `/results/<poll_id>/` | GET  | View poll results |
| `/admin/`        | GET    | Admin panel |
| `/accounts/login/` | GET/POST | User login |
| `/accounts/logout/` | GET  | User logout |

---

## Deployment (Optional) 🚀
To deploy using **Gunicorn** and **Nginx**, or **Heroku**:
```bash
pip install gunicorn
python manage.py collectstatic
```
Then follow deployment steps for your preferred platform.

---

## Author 🖊️
**Jiana Kambo**

