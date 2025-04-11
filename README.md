Here's a `README.md` file for your FastAPI-based project with user authentication and templating setup:

---

# Senthuron Real Estate Portal

## Overview
**Senthuron** is a lightweight web application built with **FastAPI** for managing user sign-up, login, and navigation across a real estate dashboard. It utilizes **Jinja2 templating** and serves static content like CSS and images, providing a smooth frontend-backend integration.

### 🔑 Features
- User Sign-Up and Login
- Email-based session validation (basic demo logic)
- Dashboard and profile navigation
- Property comparison interface
- Template-based rendering with Jinja2
- Static file serving (CSS, images)

## 🧰 Tech Stack
- **Backend**: FastAPI
- **Templating**: Jinja2
- **Database**: MongoDB (via `users_collection`)
- **Frontend**: HTML, CSS
- **Others**: Uvicorn for local dev server

## 📁 Project Structure

```
Senthuron/
│
├── static/                # Static files like CSS, images
│   ├── css/
│   └── images/
│
├── templates/             # HTML Templates (Jinja2)
│   ├── home.html
│   ├── login.html
│   ├── dashboard.html
│   ├── profile.html
│   ├── compare_property.html
│   └── reset-password.html
│
├── database.py            # MongoDB connection & users_collection
├── main.py                # Main FastAPI application
└── venv/                  # Python virtual environment
```

## 🚀 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/senthuron-real-estate.git
   cd senthuron-real-estate
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install fastapi uvicorn pymongo jinja2
   ```

4. **Run the App**
   ```bash
   uvicorn main:app --reload
   ```

5. **Visit in Browser**
   ```
   http://127.0.0.1:8000/
   ```

## 📌 Routes Summary

| Route               | Method | Description                  |
|--------------------|--------|------------------------------|
| `/`                | GET    | Homepage                     |
| `/signup`          | GET    | Sign-up page                 |
| `/signup`          | POST   | Register a new user          |
| `/login`           | GET    | Login form                   |
| `/login`           | POST   | Validate credentials         |
| `/dashboard`       | GET    | Main user dashboard          |
| `/compare_property`| GET    | Compare properties page      |
| `/profile`         | GET    | User profile view            |

## ✅ Future Enhancements
- Add JWT or session-based authentication
- Hash passwords with `bcrypt`
- Implement user role-based access (e.g., admin vs user)
- Add database models with Pydantic
- Form validation with error messaging

---
Screen Shots:
![image](https://github.com/user-attachments/assets/add982b8-f246-4105-967f-e7e10611910d)

![image](https://github.com/user-attachments/assets/0b933204-7313-4e6b-a60b-f665be9cb32e)

![image](https://github.com/user-attachments/assets/c7f1a3f5-7437-46a8-8079-d15e2baac211)


