# SmartCalc Pro

SmartCalc Pro is a Django-based web application that brings everyday, scientific, health, loan, and investment calculations into one responsive interface. It stores recent calculation history and evaluates basic arithmetic expressions through a restricted server-side parser.

## Features

- Basic arithmetic with powers and decimal values
- Scientific operations: square root, sine, cosine, tangent, and base-10 logarithm
- BMI and age calculators
- Loan EMI and discount calculators
- Simple-interest and SIP investment calculators
- Recent calculation history with a clear-history action
- Responsive web interface and production-ready static-file serving

## Technologies Used

- Python
- Django 5.2
- HTML5, CSS3, and JavaScript
- SQLite for local development
- Gunicorn as the production WSGI server
- WhiteNoise for production static files

## Local Setup

Python 3.10 or newer is recommended.

```powershell
git clone https://github.com/YOUR_USERNAME/smart_calculator.git
cd smart_calculator
py -m venv venv
.\venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
Copy-Item .env.example .env
$env:DEBUG = "True"
$env:SECRET_KEY = "local-development-secret-key"
$env:ALLOWED_HOSTS = "localhost,127.0.0.1"
py manage.py migrate
py manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser.

> Django reads these values from the process environment. The `.env` file is provided as a reference and is intentionally excluded from Git; it is not loaded automatically.

## Common Commands

```powershell
# Run application checks and tests
py manage.py check
py manage.py test

# Build production static files
py manage.py collectstatic --noinput

# Start the development server
py manage.py runserver
```

## Push to GitHub

Create an empty GitHub repository, replace the placeholder URL, and run:

```powershell
git init
git add .
git commit -m "Prepare SmartCalc Pro for deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/smart_calculator.git
git push -u origin main
```

## Deployment

The application can be deployed to any Python host that supports a WSGI start command, such as Render or Railway.

1. Push the repository to GitHub.
2. Create a new web service from the repository.
3. Use `pip install -r requirements.txt` as the build command.
4. Use `python manage.py migrate && python manage.py collectstatic --noinput` as a pre-deploy command when the platform provides one.
5. Use `gunicorn smart_calculator.wsgi:application` as the start command.
6. Configure these environment variables on the hosting platform:
   - `DEBUG=False`
   - `SECRET_KEY=<a-long-random-production-secret>`
   - `ALLOWED_HOSTS=<your-domain.example.com>`

SQLite is suitable for local development. For a persistent production deployment, configure a managed database before relying on stored calculation history.

The equivalent Linux deployment commands are:

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py check --deploy
gunicorn smart_calculator.wsgi:application --bind 0.0.0.0:${PORT:-8000}
```

## Screenshots

Add application screenshots to a `screenshots/` directory, then include them here:

```markdown
![SmartCalc Pro dashboard](screenshots/dashboard.png)
![Calculator result](screenshots/calculator-result.png)
```

## Author

**Aishwarya Gangaraj**  
Email: [aishwaryagangaraj@gmail.com](mailto:aishwaryagangaraj@gmail.com)
