FROM python

WORKDIR app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY web_service.py .

EXPOSE 8180
ENTRYPOINT ["waitress-serve", "--port=8180", "web_service:api"]
