FROM python:3.11.1

ADD src/main.py .
ADD requirements.txt .
ADD .env .

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]



