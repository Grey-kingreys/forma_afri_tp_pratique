# images de python

FROM python:3.12-slim

#information
LABEL maintainer="soulmamoudou0@gmail.com"

#creation du repertoire de l'application

WORKDIR /app

#copie les dependances de l'application et installer


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# copier le code source.

COPY app.py .
EXPOSE 5000

#Commande de lancement de l'application

CMD [ "python", "app.py" ]
