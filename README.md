## Todolist-Docker

Projet simple d'une todo list sur python afin de m'entrainer sur Docker et les principes de déployement 
- Ecrire des Dockerfiles
- Build des images
- Lancer des containers et comment les gérer
- Persister les données
- Comment utiliser Docker volumes
- Deployement sur Heroku
- Creation de workflow Github Actions
- Build / push l'image docker en ligne via GHA

Pour tester le projet sur heroku : [Todolist sur Heroku](https://todolist-docker-824700691465.herokuapp.com/ "Mon projet déployé!")

### Instructions pour lancer le projet en build 

Pour lancer le projet en build, suivez les étapes ci-dessous :

1. Clonez le repo :
  ```
  git clone https://github.com/BobbyQLF/Todolist-Docker.git
  cd Todolist-Docker
  ```

2. Build l'image Docker :
  ```
  docker build -t todolist-flask:latest .
  ```

3. Vérifiez si l'image a bien été build :
  ```
  docker image ls
  ```

4. Créez un volume pour persister les données :
  ```
  docker volume create todolist.db
  ```

5. Vérifiez si le volume a bien été créé :
  ```
  docker volume ls
  ```

6. Lancez le container en mappant le volume dans /app/db :
  ```
  docker run -dp 5000:5000 -v todolist.db:/app/db todolist-flask
  ```

7. Accédez à l'application en ouvrant http://localhost:5000 dans votre navigateur.

### Autre version

Si vous préférez utiliser une base de données PostgreSQL, suivez les étapes ci-dessous :

1. Lancez un container PostgreSQL :
  ```
  docker run -d \
    --name postgres_db \
    --network todolist-network \
    -e POSTGRES_DB=todolist \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=password \
    -v todolist_db_data:/var/lib/postgresql/data \
    postgres:14
  ```

2. Build l'image Docker :
  ```
  docker build -t todolistflask1 .
  ```

3. Lancez le container avec l'application :
  ```
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

4. Accédez à l'application en ouvrant http://localhost:5000 dans votre navigateur.

### Instructions pour lancer le projet depuis Docker Hub

Si vous préférez utiliser l'image Docker pré-construite depuis Docker Hub, suivez les étapes ci-dessous :

1. Récupérez l'image depuis Docker Hub :
  ```
  docker pull chicchino/todolist-flask
  ```

2. Créez un volume pour persister les données :
  ```
  docker volume create todolist.db
  ```

3. Vérifiez si le volume a bien été créé :
  ```
  docker volume ls
  ```

4. Lancez le container en mappant le volume dans /app/db :
  ```
  docker run -dp 5000:5000 -v todolist.db:/app/db todolist-flask
  ```

5. Accédez à l'application en ouvrant http://localhost:5000 dans votre navigateur.

### Docker Compose

Si vous préférez utiliser Docker Compose, suivez les étapes ci-dessous :

1. Lancez la commande docker-compose pour build les services :
  ```
  docker-compose build
  ```

2. Lancez les services en arrière-plan :
  ```
  docker compose up -d
  ```

3. Vérifiez l'état des services :
  ```
  docker-compose ps
  ```

4. Pour arrêter les services :
  ```
  docker-compose down
  ```

5. Accédez à l'application en ouvrant http://localhost:5000 dans votre navigateur.

### Heroku

Pour avoir acces à la base de donnée :
```
heroku pg:psql --app todolist-docker  
```

Puis faire les commandes SQL classique :
```
SELECT * FROM todo;
SELECT * FROM "user";
```