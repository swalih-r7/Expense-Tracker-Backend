# 💸 Expense Tracker — REST API Backend

<div align="center">

![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.14-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-SimpleJWT-000000?style=for-the-badge&logo=JSON%20web%20tokens)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)

**A production-ready REST API backend for personal finance management.**  
Built with Django REST Framework, PostgreSQL, and JWT authentication.

[Features](#-features) · [Tech Stack](#-tech-stack) · [Quick Start](#-quick-start) · [API Reference](#-api-reference) · [Schema](#-database-schema)

</div>

---

## 📌 Overview

Expense Tracker Backend is a fully featured REST API that powers a personal expense management application. It supports user registration and authentication, expense CRUD operations, category management, and a real-time dashboard with analytics — all secured via JWT tokens.

Designed with clean architecture, separation of concerns, and industry-standard REST conventions.

---

## ✨ Features

- 🔐 **JWT Authentication** — Secure register/login with access & refresh token flow
- 📊 **Dashboard Analytics** — Monthly totals, weekly totals, averages, highs & lows
- 🗂️ **Category Management** — Organize expenses by custom categories with icons & colors
- 💳 **Multiple Payment Methods** — Cash, UPI, Credit Card, and more
- 🛡️ **Object-Level Permissions** — Users can only access their own data
- 📄 **Auto API Docs** — Swagger UI via `drf-yasg`
- ⚙️ **Environment-based Config** — `.env` driven settings, ready for deployment

---

## 🛠 Tech Stack

| Layer | Technology | Version |
|---|---|---|
| Web Framework | Django | 4.2 |
| API Layer | Django REST Framework | 3.14 |
| Database | PostgreSQL | 16 |
| Authentication | SimpleJWT | Latest |
| DB Adapter | psycopg | 3.1 |
| API Documentation | drf-yasg (Swagger) | 1.21 |
| Image Handling | Pillow | 10.1 |

---

## 📁 Project Structure

```
expense-tracker-backend/
├── expense_tracker/        # Project settings
│   ├── settings.py         # Django configuration
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI entry point
├── apps/                   # All Django apps
│   ├── authentication/     # User auth (register, login, profile)
│   │   ├── models.py       # Custom User model
│   │   ├── views.py        # Auth API views
│   │   ├── serializers.py  # Auth serializers
│   │   └── urls.py         # Auth endpoints
│   └── expenses/           # Expense management
│       ├── models.py       # Category & Expense models
│       ├── views.py        # Expense API views
│       ├── serializers.py  # Expense serializers
│       ├── permissions.py  # Custom permissions
│       └── urls.py         # Expense endpoints
├── manage.py               # Django management
├── requirements.txt        # Dependencies
└── .env                    # Environment variables
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- PostgreSQL 16+
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/swalih-r7/Expense-Tracker-Backend.git
cd Expense-Tracker-Backend
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
# Open .env and fill in your credentials
```

```env
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=expense_tracker_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Set Up the Database

```sql
-- In psql
CREATE DATABASE expense_tracker_db;
```

### 6. Run Migrations & Create Superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 7. Start the Server

```bash
python manage.py runserver
```

API is live at: `http://127.0.0.1:8000/`  
Swagger docs at: `http://127.0.0.1:8000/swagger/`

---

## 📡 API Reference

### 🔑 Authentication

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `POST` | `/api/auth/register/` | Register a new user | ❌ |
| `POST` | `/api/auth/login/` | Login and receive JWT tokens | ❌ |
| `GET` | `/api/auth/profile/` | Retrieve current user profile | ✅ |
| `PUT` | `/api/auth/profile/` | Update user profile | ✅ |

### 💸 Expenses

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `POST` | `/api/expenses/` | Create a new expense | ✅ |
| `GET` | `/api/expenses/` | List all expenses for the user | ✅ |
| `GET` | `/api/expenses/{id}/` | Retrieve a specific expense | ✅ |
| `PUT` | `/api/expenses/{id}/` | Update an expense | ✅ |
| `DELETE` | `/api/expenses/{id}/` | Delete an expense | ✅ |

### 🗂️ Categories

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/categories/` | List all categories | ❌ |
| `POST` | `/api/categories/` | Create a category | ✅ |

### 📊 Dashboard

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/api/dashboard/summary/` | Expense analytics & summary | ✅ |

---

## 📦 Request & Response Examples

<details>
<summary><strong>POST /api/auth/register/</strong></summary>

**Request:**
```json
{
  "username": "swalih",
  "email": "swalih@example.com",
  "first_name": "Swalih",
  "last_name": "R7",
  "password": "Test123!",
  "confirm_password": "Test123!"
}
```

**Response `201 Created`:**
```json
{
  "message": "User registered successfully.",
  "user": {
    "id": 1,
    "username": "swalih",
    "email": "swalih@example.com"
  }
}
```
</details>

<details>
<summary><strong>POST /api/auth/login/</strong></summary>

**Request:**
```json
{
  "email": "swalih@example.com",
  "password": "Test123!"
}
```

**Response `200 OK`:**
```json
{
  "user": {
    "id": 1,
    "username": "swalih",
    "email": "swalih@example.com",
    "first_name": "Swalih",
    "last_name": "R7"
  },
  "access": "eyJhbGciOiJIUzI1NiIs...",
  "refresh": "eyJhbGciOiJIUzI1NiIs..."
}
```
</details>

<details>
<summary><strong>POST /api/expenses/</strong></summary>

**Request:**
```json
{
  "amount": 25.50,
  "category": 1,
  "description": "Lunch at restaurant",
  "transaction_date": "2026-05-17T13:00:00Z",
  "payment_method": "UPI"
}
```

**Response `201 Created`:**
```json
{
  "id": 1,
  "amount": "25.50",
  "category": 1,
  "description": "Lunch at restaurant",
  "transaction_date": "2026-05-17T13:00:00Z",
  "payment_method": "UPI"
}
```
</details>

<details>
<summary><strong>GET /api/dashboard/summary/</strong></summary>

**Response `200 OK`:**
```json
{
  "total_expenses": 273.25,
  "monthly_total": 273.25,
  "weekly_total": 100.75,
  "average_expense": 68.31,
  "highest_expense": 150.00,
  "lowest_expense": 12.00,
  "total_transactions": 4
}
```
</details>

---

## 🗄️ Database Schema

### Users

| Column | Type | Notes |
|--------|------|-------|
| `id` | Integer | Primary Key |
| `email` | String | Unique, used for login |
| `username` | String | Display name |
| `first_name` | String | — |
| `last_name` | String | — |

### Expenses

| Column | Type | Notes |
|--------|------|-------|
| `id` | Integer | Primary Key |
| `user_id` | ForeignKey | → Users |
| `amount` | Decimal | Expense value |
| `category_id` | ForeignKey | → Categories |
| `description` | Text | Optional note |
| `transaction_date` | DateTime | Date/time of expense |
| `payment_method` | String | CASH / UPI / CREDIT_CARD / etc. |

### Categories

| Column | Type | Notes |
|--------|------|-------|
| `id` | Integer | Primary Key |
| `name` | String | e.g., Food, Transport |
| `icon` | String | Emoji icon |
| `color` | String | Hex color code |

---

## 🔒 Authentication Flow

```
1. POST /api/auth/register/   →  Create account
2. POST /api/auth/login/      →  Receive access + refresh tokens
3. Store tokens securely      →  (e.g., HttpOnly cookie or secure storage)
4. Send with each request     →  Authorization: Bearer <access_token>
5. Token expires?             →  POST /api/auth/token/refresh/ with refresh token
```

All protected endpoints return `401 Unauthorized` if the token is missing or invalid.

---

## 🧪 Testing

### Run Test Suite

```bash
python manage.py test
```

### Manual Testing with Postman

1. Register a new user via `POST /api/auth/register/`
2. Login via `POST /api/auth/login/` — copy the `access` token
3. In Postman, set header: `Authorization: Bearer <access_token>`
4. Test expense and dashboard endpoints

> **Tip:** Import the collection via Swagger at `/swagger/` for auto-generated request templates.

---

## 📋 HTTP Status Codes

| Code | Meaning |
|------|---------|
| `200` | Success |
| `201` | Resource created |
| `400` | Validation error / bad request |
| `401` | Unauthorized — missing or invalid token |
| `403` | Forbidden — insufficient permissions |
| `404` | Resource not found |
| `500` | Internal server error |

---

## 🚢 Deployment

### Gunicorn + Nginx (Recommended)

```bash
pip install gunicorn
gunicorn expense_tracker.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

### Docker

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "expense_tracker.wsgi:application", "--bind", "0.0.0.0:8000"]
```

```bash
docker build -t expense-tracker-backend .
docker run -p 8000:8000 --env-file .env expense-tracker-backend
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Swalih R7**  
GitHub: [@swalih-r7](https://github.com/swalih-r7)

---

<div align="center">

⭐ **Star this repository if you found it helpful!**

</div>
