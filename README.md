## Todolist-Docker

To do list python pour m'entrainer avec docker / github actions

# Pour lancer le projet en build 
```
# Clone le repo
git clone https://github.com/BobbyQLF/Todolist-Docker.git
cd Todolist-Docker

# Build l'image 
docker build -t todolist-flask:latest .

# Vérifier si l'image est build
docker image ls

# Créer un volume pour persister les données
docker volume create todolist.db

# Vérifier si le volume a bien été crée
docker volume ls

# Lancer le container / Map le volume dans /app/db 
docker run -dp 5000:5000 -v todolist.db:/app/db todolist-flask

# Regarder localhost:5000
```
Autre version :
```
# Lancer un container database postgreSQL
docker run -d \                 
  --name postgres_db \
  --network todolist-network \
  -e POSTGRES_DB=todolist \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=password \
  -v todolist_db_data:/var/lib/postgresql/data \
  postgres:14

docker build -t todolistflask1 .

# Lancer container avec l'app
docker run -d \
  --name flask_app \
  --network todolist-network \
  -e FLASK_APP=app.py \
  -e FLASK_ENV=development \
  -e DATABASE_URL=postgresql://postgres:password@postgres_db:5432/todolist \
  -p 5000:5000 \
  -v $(pwd)/todolist.db:/app/todolist.db \
  todolistflask1

```

# Pour lancer le projet depuis Docker Hub
```
# Récupérer l'image 
docker pull chicchino/todolist-flask

# Créer un volume pour persister les données
docker volume create todolist.db

# Vérifier si le volume a bien été crée
docker volume ls

# Lancer le container / Map le volume dans /app/db 
docker run -dp 5000:5000 -v todolist.db:/app/db todolist-flask

# Regarder localhost:5000
```

# Docker compose
```
# Lancer la commande docker-compose
docker-compose build

docker compose up -d

# Vérifier les services 
docker-compose ps 

# Pour l'éteindre
docker-compose down

# Regarder localhost:5000
```


ancien requirements
click==7.1.2
Flask==1.1.2
Flask-SQLAlchemy==2.5.1
greenlet==1.0.0
gunicorn==20.1.0
itsdangerous==1.1.0
Jinja2==2.11.3
MarkupSafe==1.1.1
SQLAlchemy==1.4.12
Werkzeug==1.0.1
psycopg2-binary==2.9.9