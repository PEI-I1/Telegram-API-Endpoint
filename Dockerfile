FROM python:3.8
MAINTAINER PEI-i1

COPY . ./Telegram-API-Endpoint
WORKDIR Telegram-API-Endpoint

RUN pip install -r requirements.txt

CMD ["./app.py"]
