from flask import Flask, jsonify

# Création de l'application Flask
app = Flask(__name__)

# Route par défaut (Page d'accueil)
@app.route('/')
def home():
    return "🚀 API Data Engineering est en ligne ! (Version Docker)"

# Route API qui renvoie des données JSON (Exemple pour le cours)
@app.route('/api/status')
def status():
    data = {
        "cours": "Big Data & DevOps",
        "etudiants": "Licence 3",
        "status": "Succès",
        "container_ready": True
    }
    return jsonify(data)

# Point d'entrée de l'application
if __name__ == '__main__':
    # host='0.0.0.0' est CRUCIAL pour que Docker puisse exposer le port
    app.run(host='0.0.0.0', port=5000)
