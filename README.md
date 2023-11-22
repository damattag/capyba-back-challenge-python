# capyba-back-challenge
This repository is intended for the Capyba Software challenge

## Stack for this project

1. Python;
2. Django;
3. Django Rest Framework;

## Running the project

1. Be sure you have **python** and **pip** installed.

2. Clone the repository by running 
```bash 
git clone https://github.com/damattag/capyba-back-challenge-python.git
```

3. In your vs code activate virtual env
```bash 
# Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate
```

4. Install all dependencies:
```bash
pip install --upgrade pip
pip install django
pip install djangorestframework
pip install django-filter
pip install djangorestframework-simplejwt
```

5. To run the migrations, run the server as described and on a new terminal, run:
```bash
python manage.py migrate
```

6. To run the project, run the migrations as described and on terminal, run:
```bash
python manage.py runserver
```

8. Now the server should be running!
