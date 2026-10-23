
from flask import Flask,abort

app = Flask(__name__)

taches = [
    {
        "id": 1,
        "titre": "Réviser les décorateurs",
        "priorite": "haute",
        "terminee": False
    },
    {
        "id": 2,
        "titre": "Installer Flask",
        "priorite": "normale",
        "terminee": True
    },
    {
        "id": 3,
        "titre": "Lire la doc Jinja2",
        "priorite": "basse",
        "terminee": False
    }
]


@app.route("/taches/<id>")
def tache(id):
    print(type(id), id)

    for t in taches:
        if t["id"] == id:
            return t["titre"]

    return "Tâche introuvable"


