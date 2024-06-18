## Todolist-Docker

To do list python pour m'entrainer avec docker / github actions

# Pour lancer le projet en build 
```
# Clone le repo
git clone https://github.com/BobbyQLF/Todolist-Docker.git
cd Todolist-Docker

#Build l'image 
docker biuld -t todolist-flask:latest .

#Vérifier si l'image est build
docker image ls

# Créer un volume pour persister les données
docker volume create todolist.db

# Vérifier si le volume a bien été crée
docker volume ls

# Lancer le container / Map le volume dans /app/db 
docker run -dp 5000:5000 -v todolist.db:/app/db todolist-flask

# Regarder localhost:5000
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
docker-compose up -d 

# Vérifier les services 
docker-compose ps 

# Pour l'éteindre
docker-compose down

# Regarder localhost:5000
```