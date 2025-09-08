# WebSiteContainer-Test

Conteneur Docker prêt à déployer un petit site Flask de test.

## Fonctionnalités
- Consultation de la météo d'une ville en utilisant l'API gratuite [wttr.in](https://wttr.in/).
- Exemples de calculs (addition, multiplication, sinus) basés sur la bibliothèque `math`.

## Démarrage

1. Construire et lancer le conteneur :
   ```bash
   docker compose up --build
   ```
2. Ouvrir le site sur [http://localhost:5000](http://localhost:5000).
