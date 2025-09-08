from flask import Flask, render_template, request
import os
import math
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', weather=None, add_result=None, multiply_result=None, sin_result=None)


@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    info = None
    if city:
        try:
            response = requests.get(f"https://wttr.in/{city}?format=j1", timeout=5)
            data = response.json()
            current = data['current_condition'][0]
            info = {
                'temperature': current['temp_C'],
                'description': current['weatherDesc'][0]['value'],
                'humidity': current['humidity']
            }
        except Exception:
            info = {'error': 'Impossible de récupérer la météo.'}
    return render_template('index.html', weather=info, add_result=None, multiply_result=None, sin_result=None)


@app.route('/add', methods=['POST'])
def add():
    try:
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        result = a + b
    except (TypeError, ValueError):
        result = None
    return render_template('index.html', add_result=result, weather=None, multiply_result=None, sin_result=None)


@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        result = a * b
    except (TypeError, ValueError):
        result = None
    return render_template('index.html', multiply_result=result, weather=None, add_result=None, sin_result=None)


@app.route('/sin', methods=['POST'])
def sin_operation():
    try:
        x = float(request.form.get('x'))
        result = math.sin(x)
    except (TypeError, ValueError):
        result = None
    return render_template('index.html', sin_result=result, weather=None, add_result=None, multiply_result=None)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
