# Packages

django 4.2.2
djangorestframework 3.14.0
python-dotenv 1.0.0
pytest 7.3.2
pytest-django 4.5.2
black 23.3.0
flake8 6.0.0
django-mptt 0.14.0
drf-spectacular 0.26.2

# Using Django to generate secret key

./manage.py shell
from django.core.managment.utils import get_random_secret_key
print(get_random_secret_key)
l&atp1l2+cq)#^^&psh9l7e=r^m&n#mpg3-scq)!jirrdqic&s

# Test api endpoints

## GET all caterogies

curl -X 'GET' 'http://127.0.0.1:8000/api/category/' -H 'accept: _/_'

## Get all brand

curl -X 'GET' 'http://127.0.0.1:8000/api/brand/' -H 'accept: application/json'

## Get all Products

curl -X 'GET' 'http://127.0.0.1:8000/api/product/' -H 'accept: application/json'
