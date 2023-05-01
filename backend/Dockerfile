FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

ENV AWS_ACCESS_KEY_ID="AKIAS6KKQRUSWW6AZ33T"
ENV AWS_SECRET_ACCESS_KEY="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"

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
