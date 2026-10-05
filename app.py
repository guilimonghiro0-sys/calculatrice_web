from flask import Flask, render_template, request, jsonify
from models import Calculatrice

app = Flask(__name__)
calc = Calculatrice()


@app.route("/")
def accueil():
    return render_template("index.html")


@app.route("/calcul", methods=["GET", "POST"])
def calcul():
    resultat = None
    erreur = None
    nombre1 = None
    operateur = None
    nombre2 = None

    if request.method == "POST":
        try:
            nombre1 = float(request.form["nombre1"])
            operateur = request.form["operateur"]
            nombre2 = float(request.form["nombre2"])
            resultat = calc.calculer(nombre1, operateur, nombre2)
        except ValueError as e:
            erreur = str(e)

    return render_template("calcul.html",
                           resultat=resultat,
                           erreur=erreur,
                           nombre1=nombre1,
                           operateur=operateur,
                           nombre2=nombre2)


@app.route("/historique")
def historique():
    return render_template("historique.html", historique=calc.get_historique())


@app.route("/api/v1/calculer", methods=["POST"])
def api_calculer():
    donnees = request.get_json()

    if not donnees:
        return jsonify({"erreur": "Données JSON requises"}), 400

    try:
        nombre1 = float(donnees["nombre1"])
        operateur = donnees["operateur"]
        nombre2 = float(donnees["nombre2"])
        resultat = calc.calculer(nombre1, operateur, nombre2)
        return jsonify({
            "nombre1": nombre1,
            "operateur": operateur,
            "nombre2": nombre2,
            "resultat": resultat
        }), 201
    except (KeyError, TypeError):
        return jsonify({"erreur": "Champs requis : nombre1, operateur, nombre2"}), 400
    except ValueError as e:
        return jsonify({"erreur": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
