# CalculatedX Web

Application web de calculatrice développée avec Flask.

## Fonctionnalités

- **4 opérations** : addition, soustraction, multiplication, division
- **Formulaire web** : saisie de deux nombres et choix de l'opérateur
- **Historique** : consultation de tous les calculs effectués
- **API REST** : endpoint JSON pour intégration externe

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install flask
```

## Lancement

```bash
python app.py
```

Le serveur démarre sur http://127.0.0.1:5000

## Routes

| Route | Méthode | Description |
|-------|---------|-------------|
| `/` | GET | Page d'accueil |
| `/calcul` | GET, POST | Formulaire de calcul |
| `/historique` | GET | Historique des calculs |
| `/api/v1/calculer` | POST | API REST (JSON) |

## Exemple d'utilisation de l'API

```bash
curl -X POST http://127.0.0.1:5000/api/v1/calculer \
  -H "Content-Type: application/json" \
  -d '{"nombre1": 10, "operateur": "+", "nombre2": 5}'
```

Réponse :
```json
{
  "nombre1": 10.0,
  "operateur": "+",
  "nombre2": 5.0,
  "resultat": 15.0
}
```

## Structure du projet

```
tp_calculatrice_web/
├── models.py           # Classe Calculatrice (logique POO)
├── app.py              # Serveur Flask (routes et API)
├── templates/
│   ├── base.html       # Gabarit parent (navigation, CSS)
│   ├── index.html      # Page d'accueil
│   ├── calcul.html     # Formulaire de calcul
│   └── historique.html # Tableau d'historique
└── static/
    └── css/
        └── style.css   # Styles visuels
```
