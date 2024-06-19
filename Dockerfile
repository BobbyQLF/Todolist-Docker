# Python image
FROM python:3.8-slim

# Définir work directory 
WORKDIR /app

# Variables d'environnement
ENV FLASK_APP app.py
ENV FLASK_ENV development

# Copier requirements dans le container
COPY ./requirements.txt requirements.txt

# Installer requirements
RUN pip3 install -r requirements.txt

# Copier le contenu du dossier courant dans le container
COPY . .

# Commande pour lancer l'application
CMD python3 app.py