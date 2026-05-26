# InDataAI Clone

A Django-based web application clone of InDataAI website with MySQL database integration.

## Features

- Home page with hero section and services
- About Us page with company information
- Services page showcasing IT solutions
- Portfolio page displaying projects
- Events page with company events
- Contact page with form and Google Maps integration
- Responsive design with Bootstrap 5
- MySQL database for contact form submissions

## Tech Stack

- **Backend**: Django 5.2.13
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Deployment**: Render

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nithin999nth/my_indataclone.git
cd my_indataclone
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure database in `indata_project/indata_project/settings.py`

5. Run migrations:
```bash
python indata_project/manage.py migrate
```

6. Create superuser:
```bash
python indata_project/manage.py createsuperuser
```

7. Run development server:
```bash
python indata_project/manage.py runserver
```

## Deployment on Render

This project is configured for deployment on Render with MySQL database.

## License

All rights reserved.
