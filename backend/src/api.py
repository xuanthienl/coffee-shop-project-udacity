import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
from sqlalchemy.orm.exc import NoResultFound
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

with app.app_context():
    db_drop_and_create_all()

# ROUTES
'''
GET /drinks
    it should be a public endpoint
    it should contain only the drink.short() data representation
returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
    or appropriate status code indicating reason for failure
'''


@app.route("/drinks", methods=["GET"])
def drinks():
    try:
        drinks = []

        results = Drink.query.all()
        for result in results:
            drinks.append(result.short())

        return jsonify(
            {
                "success": True,
                "drinks": drinks
            }
        )
    except Exception as e:
        print(e)
        abort(500)


'''
GET /drinks-detail
    it should require the 'get:drinks-detail' permission
    it should contain the drink.long() data representation
returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
    or appropriate status code indicating reason for failure
'''


@app.route("/drinks-detail", methods=["GET"])
@requires_auth("get:drinks-detail")
def drinksDetail(payload):
    try:
        drinks = []

        results = Drink.query.all()
        for result in results:
            drinks.append(result.long())

        return jsonify(
            {
                "success": True,
                "drinks": drinks
            }
        )
    except Exception as e:
        print(e)
        abort(500)


'''
POST /drinks
    it should create a new row in the drinks table
    it should require the 'post:drinks' permission
    it should contain the drink.long() data representation
returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
    or appropriate status code indicating reason for failure
'''


@app.route("/drinks", methods=["POST"])
@requires_auth("post:drinks")
def createDrink(payload):
    try:
        body = request.get_json()

        drink = Drink(
            title=body.get("title", None),
            recipe=json.dumps(body.get("recipe", None))
        )
        drink.insert()

        return jsonify(
            {
                "success": True,
                "drinks": [drink.long()]
            }
        )
    except Exception as e:
        print(e)
        abort(422)

'''
PATCH /drinks/<id>
    where <id> is the existing model id
    it should respond with a 404 error if <id> is not found
    it should update the corresponding row for <id>
    it should require the 'patch:drinks' permission
    it should contain the drink.long() data representation
returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
    or appropriate status code indicating reason for failure
'''


@app.route("/drinks/<id>", methods=["PATCH"])
@requires_auth("patch:drinks")
def updateDrink(payload, id):
    try:
        body = request.get_json()
        title=body.get("title", None)
        recipe=body.get("recipe", None)

        drink = Drink.query.filter(Drink.id == id).one()
        if title is not None:
            drink.title=title
        if recipe is not None:
            drink.recipe=json.dumps(recipe)
        drink.update()

        return jsonify(
            {
                "success": True,
                "drinks": [drink.long()]
            }
        )
    except NoResultFound as e:
        print(e)
        abort(404)
    except Exception as e:
        print(e)
        abort(422)


'''
DELETE /drinks/<id>
    where <id> is the existing model id
    it should respond with a 404 error if <id> is not found
    it should delete the corresponding row for <id>
    it should require the 'delete:drinks' permission
returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
    or appropriate status code indicating reason for failure
'''


@app.route("/drinks/<id>", methods=["DELETE"])
@requires_auth("delete:drinks")
def deleteDrink(payload, id):
    try:
        drink = Drink.query.filter(Drink.id == id).one()
        drink.delete()

        return jsonify(
            {
                "success": True,
                "delete": id
            }
        )
    except NoResultFound as e:
        print(e)
        abort(404)
    except Exception as e:
        print(e)
        abort(500)


'''
ERRORS handlers
'''


@app.errorhandler(400)
def bad_request(error):
    return (
        jsonify({"success": False, "error": 400, "message": "Bad Request"}),
        400
    )

@app.errorhandler(404)
def not_found(error):
    return (
        jsonify({"success": False, "error": 404, "message": "Not Found"}),
        404
    )

@app.errorhandler(422)
def unprocessable_entity(error):
    return (
        jsonify({"success": False, "error": 422, "message": "Unprocessable Entity"}),
        422
    )

@app.errorhandler(405)
def method_not_allowed(error):
    return (
        jsonify({"success": False, "error": 405, "message": "Method Not Allowed"}),
        405
    )

@app.errorhandler(500)
def internal_server_error(error):
    return (
        jsonify({"success": False, "error": 500, "message": "Internal Server Error"}),
        500
    )

@app.errorhandler(AuthError)
def auth_error(error):
    return (
        jsonify({"success": False, "error": error.status_code, "message": error.error['description']}),
        error.status_code
    )
