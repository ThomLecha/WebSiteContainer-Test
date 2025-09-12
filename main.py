import os
import math
import requests
from flask import Flask, render_template, request

# Récupère la constante A depuis l’environnement
CONSTANT_A = int(os.environ.get("CONSTANT_A"))

# Récupère le port depuis l’environnement (ou 5000 par défaut)
PORT = int(os.environ.get("PORT", 5000))

# Crée l’application Flask
app = Flask(__name__)

# Définit la page d’accueil du site
@app.route("/")
def index():
    # Affiche la page index.html avec les résultats des fonctions vides
    # Remarque : render_template permet de passer des variables au template
    return render_template("index.html", constant_a=CONSTANT_A, weather=None, add_result=None, multiply_result=None, sin_result=None)

# Route pour la météo ("site.com/weather"), appelée après envoi d’un formulaire
# Remarque : Une route est une URL qui déclenche une fonction du serveur
# Remarque : "/" est la route par défaut
@app.route("/weather", methods=["POST"])
def weather():
    # Récupère la ville tapée par l’utilisateur
    city = request.form.get("city")
    info = None
    # Si une ville est fournie
    if city:
        try:
            # Envoie une requête à l’API "wttr.in" avec la ville
            response = requests.get(f"https://wttr.in/{city}?format=j1", timeout=5)
            # Transforme la réponse en JSON
            data = response.json()
            # Récupère la partie "conditions actuelles"
            current = data["current_condition"][0]
            # Prépare les infos utiles à afficher
            info = {
                "temperature": current["temp_C"],
                "description": current["weatherDesc"][0]["value"],
                "humidity": current["humidity"]
            }
        # Si la requête échoue
        except Exception:
            info = {"Erreur": "Impossible de récupérer la météo."}
    # Recharge la page avec les résultats de la météo trouvée (ou une erreur)
    return render_template("index.html", constant_a=CONSTANT_A, weather=info, add_result=None, multiply_result=None, sin_result=None)

# Route pour additionner deux nombres ("site.com/add"), appelée après envoi d’un formulaire
@app.route("/add", methods=["POST"])
def add():
    try:
        # Récupère et convertit le premier nombre
        a = float(request.form.get("a"))
        # Récupère et convertit le second nombre
        b = float(request.form.get("b"))
        # Fait l’addition
        result = a + b
    # Si la conversion échoue
    except (TypeError, ValueError):
        result = None
    # Recharge la page avec le résultat de l'addition trouvé (ou une erreur)
    return render_template("index.html", constant_a=CONSTANT_A,  weather=None, add_result=result, multiply_result=None, sin_result=None)

# Route pour multiplier deux nombres ("site.com/multiply"), appelée après envoi d’un formulaire
@app.route("/multiply", methods=["POST"])
def multiply():
    try:
        # Récupère et convertit le premier nombre
        a = float(request.form.get("a"))
        # Récupère et convertit le second nombre
        b = float(request.form.get("b"))
        # Fait la multiplication
        result = a * b
    # Si la conversion échoue
    except (TypeError, ValueError):
        result = None
    # Recharge la page avec le résultat de la multiplication trouvé (ou une erreur)
    return render_template("index.html", constant_a=CONSTANT_A, weather=None, add_result=None, multiply_result=result, sin_result=None)

# Route pour avoir le sinus d'un nombre ("site.com/sin"), appelée après envoi d’un formulaire
@app.route("/sin", methods=["POST"])
def sin_operation():
    try:
        # Récupère et convertit le nombre
        x = float(request.form.get("x"))
        # Calcule le sinus
        result = math.sin(x)
    # Si la conversion échoue
    except (TypeError, ValueError):
        result = None
    # Recharge la page avec le résultat du sinus trouvé (ou une erreur)
    return render_template("index.html", constant_a=CONSTANT_A, sin_result=result, weather=None, add_result=None, multiply_result=None)

# Lance l’application Flask accessible depuis l’extérieur
app.run(host="0.0.0.0", port=PORT)