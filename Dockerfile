FROM python:3.8-alpine

WORKDIR /

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python3 -m spacy download en_core_web_sm

EXPOSE 80

CMD [ "python3", "app.py" ]