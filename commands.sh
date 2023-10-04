pip install djangorestframework
pip install djangorestframework-jwt

django-admin startproject BackendAssignment

cd BackendAssignment

python manage.py startapp api
python manage.py makemigrations
python manage.py migrate
