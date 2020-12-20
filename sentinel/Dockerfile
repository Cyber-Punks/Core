FROM python

WORKDIR app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY server .

EXPOSE 8000
RUN cd server
RUN python manage.py runserver