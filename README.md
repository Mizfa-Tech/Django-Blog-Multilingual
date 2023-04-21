# Django-Blog-Multilingual

Django-Blog-Multilingual is a blog web application built with the Django web framework. This application is designed to be multilingual, allowing users to create and read blog posts in multiple languages.

## Features
- Multilingual support: Users can create and read blog posts in multiple languages.
- User authentication: Users can create accounts and log in to create, edit, and delete their own blog posts.
- Admin dashboard: Administrators can manage all blog posts and user accounts from the admin dashboard.
- Responsive design: The web application is designed to be responsive, adapting to different screen sizes and devices.

## Installation
1. Clone the repository:

```bash 
git clone https://github.com/Mizfa-Tech/Django-Blog-Multilingual

```
2. Navigate to the project directory:
```bash 
cd Django-Blog-Multilingual
```
3. Create a virtual environment:
```bash 
python -m venv env
```

4. Activate the virtual environment:
On Windows:
```bash 
env\Scripts\activate
```
On macOS and Linux:
```bash 
source env/bin/activate
```


5. Install the required packages:
```bash 
pip install -r requirements.txt
```

6. Run the database migrations & create superuser:
```bash 
python manage.py migrate
python manage.py createsuperuser
```

7. Run the development server:
```bash 
python manage.py runserver
```

8. Open the web application in your browser:
```bash
http://localhost:8000/
```
