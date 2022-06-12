from config import app, db
from models import Site
from flask import request, jsonify


@app.route("/hello")
def hello():
    return "Hello World"


def to_json(site):
    return {
        "id": site.id,
        "nom": site.nom,
        "image": site.image,
        "description": site.description,
        "note": site.note
    }


def to_json_list(sites):
    return jsonify([to_json(site) for site in sites])


@app.route("/sites", methods=["POST"])
def create():
    site_json = request.json
    site = Site(
        nom=site_json["nom"],
        image=site_json["image"],
        description=site_json["description"],
        note=site_json["note"],
    )
    db.session.add(site)
    db.session.commit()
    return to_json(site)


@app.route("/sites/<int:id>", methods=["PUT"])
def update(id):
    site_json = request.json
    site = Site.query.get(id)
    if site_json["nom"]:
        site.nom = site_json["nom"]
    if site_json["image"]:
        site.image = site_json["image"]
    if site_json["description"]:
        site.description = site_json["description"]
    if site_json["note"]:
        site.note = site_json["note"]

    db.session.add(site)
    db.session.commit()
    return to_json(site)


@app.route("/sites/<int:id>", methods=["DELETE"])
def delete(id):
    site = Site.query.get(id)
    db.session.delete(site)
    db.session.commit()
    return "Site touristique "+site.nom+" supprimé avec succès"


@app.route("/sites/<int:id>", methods=["GET"])
def get(id):
    site = Site.query.get(id)
    return to_json(site)


@app.route("/sites", methods=["GET"])
def get_all():
    sites = Site.query.all()
    return to_json_list(sites)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=50000, debug=True)
