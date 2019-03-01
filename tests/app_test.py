from nose.tools import assert_true
import requests

baseUrl = "http://127.0.0.1"
#baseUrl = "http://localhost:5000"
UUID = None


def test_get_all_requests():
    global baseUrl
    response = requests.get('%s/request' % (baseUrl))
    assert_true(response.ok)


def test_get_individual_request():
    global baseUrl
    response = requests.get(
        '%s/request/04cfc704-acb2-40af-a8d3-4611fab54ada' % (baseUrl))
    assert_true(response.ok)


def test_get_individual_request_404():
    global baseUrl
    response = requests.get('%s/request/an_incorrect_id' % (baseUrl))
    assert_true(response.status_code == 404)


def test_add_new_record():
    global baseUrl
    global UUID
    payload = {'title': 'Good & Bad Book', 'email': 'testuser3@test.com'}
    response = requests.post('%s/request' % (baseUrl), json=payload)
    UUID = str(response.json()['request']['id'])
    assert_true(response.status_code == 201)


def test_add_new_record_bad_email_format():
    global baseUrl
    global UUID
    payload = {'title': 'Good & Bad Book', 'email': 'badEmailFormat'}
    response = requests.post('%s/request' % (baseUrl), json=payload)
    assert_true(response.status_code == 400)


def test_add_new_record_bad_title_key():
    global baseUrl
    global UUID
    payload = {'badTitleKey': 'Good & Bad Book', 'email': 'testuser4@test.com'}
    response = requests.post('%s/request' % (baseUrl), json=payload)
    assert_true(response.status_code == 400)


def test_add_new_record_no_email_key():
    global baseUrl
    global UUID
    payload = {'title': 'Good & Bad Book'}
    response = requests.post('%s/request' % (baseUrl), json=payload)
    assert_true(response.status_code == 400)


def test_add_new_record_no_title_key():
    global baseUrl
    global UUID
    payload = {'email': 'testuser5@test.com'}
    response = requests.post('%s/request' % (baseUrl), json=payload)
    assert_true(response.status_code == 400)


def test_add_new_record_unicode_title():
    global baseUrl
    global UUID
    payload = {'title': '▚Ⓜ⌇⇲', 'email': 'testuser5@test.com'}
    response = requests.post('%s/request' % (baseUrl), json=payload)
    assert_true(response.ok)


def test_add_new_record_no_payload():
    global baseUrl
    global UUID
    payload = None
    response = requests.post('%s/request' % (baseUrl), json=payload)
    assert_true(response.status_code == 400)


def test_get_new_record():
    global baseUrl
    global UUID
    url = '%s/request/%s' % (baseUrl, UUID)
    response = requests.get(url)
    assert_true(response.ok)


def test_delete_new_record():
    global baseUrl
    global UUID
    response = requests.delete('%s/request/%s' % (baseUrl, UUID))
    assert_true(response.status_code == 204)


def test_delete_new_record_404():
    global baseUrl
    global UUID
    response = requests.delete('%s/request/%s' % (baseUrl, UUID))
    assert_true(response.status_code == 404)
