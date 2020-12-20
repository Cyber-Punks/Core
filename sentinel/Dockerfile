FROM python

WORKDIR /app/server

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY manage.py .
COPY google_platform_key.json .
ENV GOOGLE_APPLICATION_CREDENTIALS="google_platform_key.json"
WORKDIR /app/server/sentinel_backend
COPY sentinel_backend .

EXPOSE 8000
WORKDIR /app/server
ENTRYPOINT python manage.py runserver
#ENTRYPOINT sh