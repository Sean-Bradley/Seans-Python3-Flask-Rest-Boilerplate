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

