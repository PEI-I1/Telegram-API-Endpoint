FROM python:3.8
MAINTAINER PEI-i1

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/PEI-I1/Telegram-API-Endpoint.git

WORKDIR Telegram-API-Endpoint

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
