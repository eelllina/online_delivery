FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


ENV PYTHONUNBUFFERED=1


RUN python manage.py migrate


CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]

