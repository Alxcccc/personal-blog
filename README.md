
# Personal Blog Django

personal blog to write and publish articles on various topics. The Web is built with **Django** and uses **MySqLite** as the database for data storage.

Credits of idea for: https://roadmap.sh/projects/personal-blog


## Features

- **Post Management**: CRUD (Create, Read, Update, Delete) operations for blog posts.
- **Simple Auth**: The views post management only avaible for Admins, guest only watch post.


## Technologies
- Python 3.13
- Django 5.1.4
- MySqLite
## Installation

To run the app, ensure you have Python installed and follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Alxcccc/personal-blog.git

cd personal-blog
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Configure Environment Variables:
- Create a .env file: Inside core directory of your project, create a file named .env and add the following lines (you will replace your_generated_secret_key later):
```bash
SECRET_KEY='your_generated_secret_key'
DEBUG=True
```
- Instructions to Generate a New Secret Key: Users can generate a new secret key by creating a temporary Python script, for example, generate_secret_key.py, and adding the following code:
```bash
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```
- Then, they should run this script from the terminal:
```bash
python generate_secret_key.py
```
- The generated secret key will be displayed in the console. Users should copy this key.
- Update the .env File: Users should paste the copied secret key into their .env file, replacing your_generated_secret_key:
```bash
SECRET_KEY='new_generated_key'
DEBUG=True

```

5. Set up the database:
- Apply database migrations to set up the database schema:
```bash
python manage.py migrate
```
- Create a Superuser (Optional): If you need access to the Django admin interface, create a superuser account:
```bash
python manage.py createsuperuser
```


    
## Usage

Run the Development Server:

- Start the development server:
```bash
python manage.py runserver
```
- Access the application by navigating to http://127.0.0.1:8000/ in your web browser.


