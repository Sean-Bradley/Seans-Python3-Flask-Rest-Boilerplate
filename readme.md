## Seans Python3 Flask Rest Boilerplate

### To Setup and Start
```bash
docker-compose up
```

### Get All Request Records
```bash
curl -X GET http://127.0.0.1/request
```

### Get One Request Record
```bash
curl -X GET http://127.0.0.1/request/04cfc704-acb2-40af-a8d3-4611fab54ada
```

### Add A New Record
```bash
curl -X POST http://127.0.0.1/request -H 'Content-Type: application/json' -d '{"title":"Good & Bad Book", "email": "testuser3@test.com"}'
```

### Delete A Record
```bash
curl -X DELETE http://127.0.0.1/request/04cfc704-acb2-40af-a8d3-4611fab54ada
```



## Unit Test with Nose
```bash
nosetests --verbosity=2
```
**NOTE: the tests expect your are running the app via `docker-compose -up` and on the same computer.**
If you run the app from python directly,
eg,
```bash
python app.py --debug
```
The endpoint will be http://localhost:5000 rather than the endpoint exposed via running it in the docker-compose. You should change the baseUrl in the script /tests/app_test.py to suit your environment

### Test Output
```bash
$ nosetests --verbosity=2
app_test.test_get_all_requests ... ok
app_test.test_get_individual_request ... ok
app_test.test_get_individual_request_404 ... ok
app_test.test_add_new_record ... ok
app_test.test_add_new_record_bad_email_format ... ok
app_test.test_add_new_record_bad_title_key ... ok
app_test.test_add_new_record_no_email_key ... ok
app_test.test_add_new_record_no_title_key ... ok
app_test.test_add_new_record_unicode_title ... ok
app_test.test_add_new_record_no_payload ... ok
app_test.test_get_new_record ... ok
app_test.test_delete_new_record ... ok
app_test.test_delete_new_record_404 ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.188s

OK
```

## Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](
    https://heroku.com/deploy?template=https://github.com/Sean-Bradley/Seans-Python3-Flask-Rest-Boilerplate)

You can also test this api on heroku
https://seans-python3-flask-rest.herokuapp.com/request

use the above curl commands replacing `http://127.0.0.1` with `https://seans-python3-flask-rest.herokuapp.com`

