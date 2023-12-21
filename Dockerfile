FROM python:3.9-alpine3.19

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]