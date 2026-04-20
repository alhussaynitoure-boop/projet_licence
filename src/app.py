"""
Point d'entrée principal de l'application Flask.
Ce fichier démarre le serveur web et charge la configuration.
"""

# Import des dépendances
from flask import Flask, render_template

# Création de l'application Flask
# template_folder='templates' indique où chercher les fichiers HTML
app = Flask(__name__, template_folder='templates')


# Route de la page d'accueil
@app.route('/')
def accueil():
    """
    Page d'accueil du site.
    Affiche le template index.html avec le layout commun.
    """
    return render_template('index.html')


@app.route('/produit')
def produit():
    """
    Page de détail produit (Template).
    """
    return render_template('produit.html')


# Point d'entrée pour lancer le serveur
if __name__ == '__main__':
    # Mode debug=True : recharge automatiquement quand on modifie le code
    app.run(debug=True, host='0.0.0.0', port=5000)
