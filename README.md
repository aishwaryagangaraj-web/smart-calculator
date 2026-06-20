# 🧮 SmartCalc Pro

SmartCalc Pro is a modern Django-based web application that combines multiple calculators into a single responsive platform. It provides everyday, scientific, health, financial, and investment calculation tools with a clean user interface and calculation history tracking.

---

## 🌐 Live Demo

🔗 https://smart-calculator-g5th.onrender.com

---

## 📌 Project Overview

SmartCalc Pro was developed to provide users with a centralized platform for performing different types of calculations without switching between multiple applications.

The application supports:

* Basic arithmetic operations
* Scientific calculations
* BMI calculations
* Loan EMI calculations
* Discount calculations
* Age calculations
* Interest calculations
* SIP investment calculations

The project is built using Django and follows production-ready deployment practices using Gunicorn and WhiteNoise.

---

## ✨ Features

### 🧮 Basic Calculator

* Addition
* Subtraction
* Multiplication
* Division
* Decimal calculations
* Power operations

### 📐 Scientific Calculator

* Square Root
* Logarithm (Base 10)
* Sine
* Cosine
* Tangent
* Mathematical constants

### ⚕️ BMI Calculator

* Body Mass Index calculation
* Health category determination
* Weight analysis

### 🏦 Loan EMI Calculator

* Monthly EMI calculation
* Loan repayment estimation
* Financial planning assistance

### 🏷️ Discount Calculator

* Discount amount calculation
* Final payable amount
* Savings estimation

### 🎂 Age Calculator

* Exact age calculation
* Years, months, and days breakdown

### 💰 Interest Calculator

* Simple Interest calculation
* Investment growth estimation

### 📈 SIP Calculator

* Monthly investment planning
* Future investment value estimation

### 📝 Calculation History

* Stores recent calculations
* Quick reference for previous results
* Clear history functionality

### 📱 Responsive Design

* Mobile-friendly interface
* Tablet support
* Desktop optimized layout

---

## 🚀 Project Highlights

* Multi-functional calculator platform
* Secure server-side expression evaluation
* Production-ready Django deployment
* Responsive modern UI
* Calculation history management
* WhiteNoise static file optimization
* Render cloud deployment
* Clean and maintainable codebase

---

## 🛠️ Technologies Used

### Backend

* Python 3
* Django 5.2

### Frontend

* HTML5
* CSS3
* JavaScript

### Database

* SQLite3

### Production Tools

* Gunicorn
* WhiteNoise

### Deployment

* Render

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
smart_calculator/
│
├── calculator/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── smart_calculator/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── staticfiles/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Local Setup

### Prerequisites

* Python 3.10+
* Git
* pip

### Clone Repository

```bash
git clone https://github.com/aishwaryagangaraj-web/smart-calculator.git
cd smart-calculator
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Database Migrations

```bash
python manage.py migrate
```

### Start Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## 📋 Common Commands

### Run Development Server

```bash
python manage.py runserver
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create New Migration

```bash
python manage.py makemigrations
```

### Run Tests

```bash
python manage.py test
```

### Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Check Project Configuration

```bash
python manage.py check
```

---

## 🚀 Deployment (Render)

### Build Command

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

### Start Command

```bash
gunicorn smart_calculator.wsgi:application
```

### Environment Variables

```env
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=smart-calculator-g5th.onrender.com
```

---
## 📸 Screenshots

### Home Page

![SmartCalc Pro Home](calculator/static/calculator/images/Screenshot%202026-06-20%20103902.png)



## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Django Web Development
* URL Routing
* Django Templates
* Static File Management
* Form Handling
* Production Deployment
* Git & GitHub Workflow
* Cloud Hosting with Render
* Responsive Web Design
* Python Backend Development

---

## 🔮 Future Enhancements

* User Authentication
* Dark Mode
* Calculation Export (PDF)
* Graph Plotting Calculator
* Currency Converter
* Unit Converter
* Scientific Expression Parser
* Calculation Analytics Dashboard

---

## 👩‍💻 Author

### Aishwarya Gangaraj

🎓 Computer Science Engineering (AI & ML)

📧 Email:
[aishwaryagangaraj@gmail.com](mailto:aishwaryagangaraj@gmail.com)

💻 GitHub:
https://github.com/aishwaryagangaraj-web

🔗 LinkedIn:
https://www.linkedin.com/in/aishwarya-gangaraj-b7659328a

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support helps improve and maintain the project.

---

## 📜 License

This project is licensed under the MIT License.
