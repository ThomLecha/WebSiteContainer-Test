# Utilise une image Python légère compatible ARM
FROM python:3.11-alpine

WORKDIR /app

# Installe les dépendances
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code source
COPY . .

EXPOSE 5000

CMD ["python", "main.py"]
