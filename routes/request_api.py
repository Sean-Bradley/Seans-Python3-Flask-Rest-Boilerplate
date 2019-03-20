from flask import jsonify, abort, request, Blueprint
from datetime import datetime, timedelta
import uuid
from validate_email import validate_email
request_api = Blueprint('request_api', __name__)


def get_blueprint():
    return request_api


bookRequests = {
    "8c36e86c-13b9-4102-a44f-646015dfd981": {
        'title': u'Good Book',
        'email': u'testuser1@test.com',
        'timestamp': (datetime.today() - timedelta(1)).timestamp()
    },
    "04cfc704-acb2-40af-a8d3-4611fab54ada": {
        'title': u'Bad Book',
        'email': u'testuser2@test.com',
        'timestamp': (datetime.today() - timedelta(2)).timestamp()
    }
}


@request_api.route('/request', methods=['GET'])
def get_records():
    return jsonify(bookRequests)


@request_api.route('/request/<string:id>', methods=['GET'])
def get_record_by_id(id):
    if id not in bookRequests:
        abort(404)
    return jsonify(bookRequests[id])


@request_api.route('/request', methods=['POST'])
def create_record():
    if not request.get_json():
        abort(400)
    data = request.get_json(force=True)

    if not data.get('email'):
        abort(400)
    if not validate_email(data['email']):
        abort(400)
    if not data.get('title'):
        abort(400)

    newUUID = str(uuid.uuid4())
    bookRequest = {
        'title': data['title'],
        'email': data['email'],
        'timestamp': datetime.now().timestamp()
    }
    bookRequests[newUUID] = bookRequest
    # HTTP 201 Created
    return jsonify({"id": newUUID}), 201


@request_api.route('/request/<string:id>', methods=['PUT'])
def edit_record(id):
    if id not in bookRequests:
        abort(404)

    if not request.get_json():
        abort(400)
    data = request.get_json(force=True)

    if not data.get('email'):
        abort(400)
    if not validate_email(data['email']):
        abort(400)
    if not data.get('title'):
        abort(400)

    bookRequest = {
        'title': data['title'],
        'email': data['email'],
        'timestamp': datetime.now().timestamp()
    }

    bookRequests[id] = bookRequest
    return jsonify(bookRequests[id]), 200


@request_api.route('/request/<string:id>', methods=['DELETE'])
def delete_record(id):
    if id not in bookRequests:
        abort(404)

    del bookRequests[id]

    return '', 204
