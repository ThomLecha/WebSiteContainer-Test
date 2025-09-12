# Utilise une image Linux Alpine pour Python (image légère)
FROM python:3.13-alpine

# Défini le répertoire de travail dans le container (qui est aussi le répertoire courant dans le container)
WORKDIR /app

# Copie le fichier des dépendances Python de l'hôte vers le répertoire de travail dans le container
COPY ./requirements.txt ./requirements.txt

# Installe les dépendances python
RUN pip install --no-cache-dir -r requirements.txt

# Copie le répertoire courant l'hôte vers le répertoire de travail dans le container ("." = tout le contenu du répertoire courant)
COPY . .

# Expose le port 5000 du container (uniquement de la documentation, le vrai paramétrage se fait avec docker run -p ou le docker-compose)
EXPOSE 5000

# Exécute la commande par défaut pour exécuter l'application (litérallement la commande "python main.py")
CMD ["python", "main.py"]