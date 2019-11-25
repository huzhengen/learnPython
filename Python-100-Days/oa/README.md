Windows

```
python -m venv venv
source venv/Scripts/activate

pip install django

django-admin startproject oa .

python manage.py runserver 127.0.0.1:8089
python manage.py runserver 8089
http://127.0.0.1:8089/
```