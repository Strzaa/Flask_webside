FROM python:3.8-slim

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

COPY . .

WORKDIR /app

RUN pip install -r requirements.txt

RUN mkdir exel
RUN chmod -R 777 exel

EXPOSE 5000

CMD ["flask","run"]
#CMD [ "sleep","infinity" ]
