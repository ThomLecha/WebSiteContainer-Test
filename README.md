# WebSiteContainer-Test

Conteneur Docker bien documenté et prêt à déployer un petit site Python Flask de test.

## Fonctionnalités
- Consultation de la météo d'une ville en utilisant l'API gratuite [wttr.in](https://wttr.in/).
- Exemples de calculs (addition, multiplication, sinus) basés sur la bibliothèque `math`.

## Démarrage

1. Cloner ce dépôt sur votre machine
   ```
   git clone https://github.com/ThomLecha/WebSiteContainer-Test.git
   ```
   
2. Construire et lancer le conteneur :
   ```
   cd WebSiteContainer-Test
   docker compose up --build
   ```
3. Ouvrir le site sur [http://localhost:5000](http://localhost:5000).
