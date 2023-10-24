# M10_Django

## Для проекту потрібно встановити програми:

django-admin startproject quotes_app

 docker run --name quotesapp-postgres -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres


 pipenv install psycopg2

python manage.py createsuperuser

python manage.py startapp quotes

python manage.py makemigrations

python manage.py migrate

- MongoDB: Для роботи з базою даних MongoDB. Можна завантажити з офіційного сайту MongoDB: https://www.mongodb.com/try/download/community
  
## Запуск проекту

Створіть конфігураційний файл ``config.ini`` з налаштуваннями для підключення до вашої MongoDB бази даних. Ваш файл ``config.ini`` може виглядати так:

```
[mongodb]
uri = mongodb+srv://username:password@cluster.mongodb.net/mydatabase

```