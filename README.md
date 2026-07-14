# README.md
# 🚌 Bus Ticketing Management System

A modern **Bus Ticketing Management System** developed using **Python, Flask, PostgreSQL, SQLAlchemy, Alembic, Bootstrap 5, and Jinja2**. This project demonstrates a complete bus reservation system with passenger management, ticket booking, payment processing, refund management, QR Code ticket generation, and reporting.

---

# 📌 Project Information

| Item | Details |
|------|---------|
| Project Name | Bus Ticketing Management System |
| Framework | Flask |
| Language | Python 3.x |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migration | Alembic |
| Frontend | HTML5, CSS3, Bootstrap 5, Jinja2 |
| Authentication | Flask-Login |
| Security | CSRF Protection, Password Hashing |
| QR Code | qrcode + Pillow |

---

# 🎯 Project Objectives

The purpose of this project is to:

- Automate bus ticket booking
- Manage buses and routes
- Schedule bus trips
- Manage passengers
- Generate QR Code tickets
- Process payments and refunds
- Produce daily sales reports
- Demonstrate Flask CRUD operations
- Teach SQLAlchemy Relationships & Database Migration

---

# 🚀 Technologies Used

- Python 3.12+
- Flask
- PostgreSQL
- SQLAlchemy
- Flask-Migrate
- Alembic
- Flask-WTF
- Flask-Login
- Bootstrap 5
- Font Awesome
- Jinja2
- qrcode
- Pillow

---

# 📂 Project Structure

```
BusTicketingSystem
│
├── app
│   ├── forms
│   ├── models
│   ├── routes
│   ├── services
│   ├── templates
│   ├── static
│   │     ├── css
│   │     ├── js
│   │     ├── images
│   │     └── qrcodes
│   ├── utils
│   └── __init__.py
│
├── migrations
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

# 📦 Modules

## Authentication

- User Registration
- User Login
- Logout
- Password Encryption
- Role-based Authentication

---

## Dashboard

- Total Bus
- Total Routes
- Total Schedules
- Total Passengers
- Total Bookings
- Total Tickets
- Total Payments
- Total Refunds
- Revenue Summary

---

## Bus Management

- Add Bus
- Edit Bus
- Delete Bus
- View Bus
- Search Bus

---

## Route Management

- Add Route
- Edit Route
- Delete Route
- View Route

---

## Schedule Management

- Add Schedule
- Edit Schedule
- Delete Schedule
- View Schedule

---

## Passenger Management

- Add Passenger
- Edit Passenger
- Delete Passenger
- Search Passenger

---

## Seat Management

- Auto Generate Seats
- Seat Availability
- Seat Status
- Seat Booking

---

## Booking Management

- Create Booking
- Edit Booking
- Cancel Booking
- Booking History
- Seat Allocation

---

## Payment Management

- Cash Payment
- Card Payment
- Mobile Banking
- Payment Status

---

## Refund Management

- Create Refund
- Refund History
- Refund Approval

---

## Ticket Management

- Generate Ticket
- Print Ticket
- QR Code Ticket
- Ticket Verification

---

## Employee Management

- Add Employee
- Edit Employee
- Delete Employee
- Employee Report

---

## Reports

- Sales Report
- Booking Report
- Passenger Report
- Bus Report
- Route Report
- Schedule Report
- Seat Report
- Ticket Report
- Payment Report
- Refund Report
- Employee Report

---

# 🗄 Database Tables

- Users
- Bus
- Route
- Schedule
- Passenger
- Seat
- Booking
- Booking Detail
- Ticket
- Payment
- Refund
- Employee

---

# 🔗 Database Relationships

```
Bus
   │
   └──────< Schedule >────── Route
                  │
                  │
                  ▼
              Booking
             /        \
            /          \
       Ticket        Payment
```

---

# 🔐 User Roles

## Administrator

- Full System Access
- Manage Users
- Manage Bus
- Manage Route
- Manage Schedule
- Reports
- Employees
- Payments
- Refunds

---

## Employee

- Passenger Registration
- Booking
- Ticket Issue
- Payment
- Refund

---

## Passenger

- Registration
- Book Ticket
- View Ticket
- Print Ticket

---

# 📱 QR Code Ticket

Each ticket contains:

- Ticket Number
- Booking Number
- Passenger Name
- Bus Information
- Route Information
- Journey Date
- Seat Number
- Verification Link

---

# 📊 Sample Reports

- Daily Sales
- Booking Summary
- Route Report
- Bus Report
- Ticket Report
- Payment Report
- Refund Report

---

# ▶️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/BusTicketingSystem.git
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

---

## Install Packages

```bash
pip install -r requirements.txt
```

---

## Configure Database

Update `config.py`

```python
SQLALCHEMY_DATABASE_URI="postgresql://postgres:1234@localhost/bus_ticketing"
```

---

## Migration

```bash
flask db init
```

```bash
flask db migrate -m "Initial Migration"
```

```bash
flask db upgrade
```

---

## Run Application

```bash
python run.py
```

or

```bash
flask run
```

---

# 🌐 Application URL

```
http://127.0.0.1:5000
```

---

# 📋 Demonstration Data

- 5 Sample Buses
- 5 Routes
- 5 Passengers
- 10 Ticket Bookings
- 2 Cancelled Bookings
- Daily Sales Report

---

# 🎓 Learning Outcomes

This project demonstrates:

- Flask Blueprint
- CRUD Operations
- PostgreSQL Integration
- SQLAlchemy Relationships
- Alembic Migration
- Flask-WTF Forms
- Flask-Login Authentication
- QR Code Generation
- Bootstrap Dashboard
- Report Generation

---

# 📄 License

This project is developed for educational purposes.

---

# 👨‍💻 Developer

**Md. Rafiqul Islam**

Founder & CEO

**Rafiqul Islam Ltd**

United Kingdom

Email: info@openjanalait.com

LinkedIn: https://www.linkedin.com/in/openjanalait/

GitHub: https://github.com/yourusername

---

# ⭐ Acknowledgements

- Flask
- SQLAlchemy
- PostgreSQL
- Bootstrap
- Font Awesome
- Python Community

---

## Version

**Version:** 1.0.0

**Last Updated:** July 2026