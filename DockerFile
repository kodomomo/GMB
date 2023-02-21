FROM python:3.9

COPY .env ./
COPY run.py ./
COPY requirements.txt ./
COPY app ./app

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "run:app","--host", "0.0.0.0"]