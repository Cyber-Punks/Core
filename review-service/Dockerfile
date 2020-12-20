FROM python

WORKDIR app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY web_service.py .

EXPOSE 8180
ENTRYPOINT ["waitress-serve", "web_service:api"]
