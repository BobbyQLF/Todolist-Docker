# Python image
FROM python:3.8-slim
# Work directory 
WORKDIR /

# variables environnements 
ENV FLASK_APP app.py
ENV FLASK_ENV development

# copier requirements dans le container
COPY ./requirements.txt /requirements.txt

# install requirements
RUN pip3 install -r requirements.txt

RUN mkdir app
WORKDIR /app

# copy the project artefects into the container under the root directory
COPY . .

# the command to run once we run the container 
CMD python3 app.py