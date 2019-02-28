# from app import app
from flask import jsonify, abort, request, Blueprint
from datetime import datetime, timedelta
import uuid
from validate_email import validate_email

request_api = Blueprint('request_api', __name__)


def get_blueprint():
    return request_api


bookRequests = [
    {
        'id': "8c36e86c-13b9-4102-a44f-646015dfd981",
        'title': u'Good Book',
        'email': u'testuser1@test.com',
        'timestamp': datetime.today() - timedelta(1)  # yesterday
    },
    {
        'id': "04cfc704-acb2-40af-a8d3-4611fab54ada",
        'title': u'Bad Book',
        'email': u'testuser2@test.com',
        'timestamp': datetime.today() - timedelta(2)  # 2 days ago
    }
]


@request_api.route('/request', methods=['GET'])
def get_records():
    try:
        return jsonify({'requests': bookRequests})
    except Exception as e:
        abort(400)


@request_api.route('/request/<string:id>', methods=['GET'])
def get_record_by_id(id):
    notFound = False
    try:
        req = [req for req in bookRequests if req['id'] == id]
        if len(req) == 0:
            notFound = True
    except Exception as e:
        print("in error")
        abort(400)

    if notFound:
        abort(404)
    else:
        return jsonify({'request': req[0]})


@request_api.route('/request', methods=['POST'])
def create_record():
    if request.get_json():
        data = request.get_json(force=True)
        if data['email'] and validate_email(data['email']):
            if data['title']:
                newUUID = str(uuid.uuid4())
                print(newUUID)
                print(str(datetime.now()))
                bookRequest = {
                    'id': newUUID,
                    'title': data['title'],
                    'email': data['email'],
                    'timestamp': datetime.now()
                }
                print(bookRequest)
                bookRequests.append(bookRequest)
                # HTTP 201 Created
                return jsonify({'request': bookRequest}), 201
            else:
                abort(400)
        else:
            abort(400)
    else:
        abort(400)


@request_api.route('/request/<string:id>', methods=['DELETE'])
def delete_record(id):
    notFound = False
    try:
        req = [req for req in bookRequests if req['id'] == id]
        if len(req) == 0:
            notFound = True
    except Exception as e:
        abort(400)

    if notFound:
        abort(404)
    else:
        bookRequests.remove(req[0])
        # HTTP 204 No Content
        return ('', 204)
