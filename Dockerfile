FROM python:3


COPY /api /main

WORKDIR /main

RUN pip install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0 --port ${PORT}

