FROM python

WORKDIR app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY scraper.py .

EXPOSE 8080
ENTRYPOINT ["waitress-serve", "scraper:api"]
