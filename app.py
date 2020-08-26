"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


@app.route("/api/cupcakes")
def list_cupcakes():
    """Return all cupcakes in system.

    Returns JSON like:
        {cupcakes: [{id, flavor, rating, size, image}, ...]}
    """

    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


# @app.route('/api/cupcakes/<int:id>')
# def get_cupcake(id):
#     """Returns JSON for one cupcake in particular"""
#     cupcake = Cupcake.query.get_or_404(id)
#     return jsonify(cupcake=cupcake.serialize())


# @app.route('/api/cupcakes', methods=["POST"])
# def create_cupcake():
#     """Creates a new cupcake and returns JSON of that created cupcake"""
#     new_cupcake = Cupcake(flavor=request.json["flavor"])
#     db.session.add(new_cupcake)
#     db.session.commit()
#     response_json = jsonify(cupcake=new_cupcake.serialize())
#     return (response_json, 201)
