FROM python
WORKDIR /app
# COPY ./app /app
COPY ./app/requirements.txt /app
COPY ./app/wait-for-it.sh /app

RUN pip install -r requirements.txt