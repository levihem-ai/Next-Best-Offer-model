# Next-Best-Offer-model
Модель для генерации персональных маркетинговых предложений по ТЗ Газпромбанк Тех

## client - ReactApp

To run dev-server execute the folowing commands:
```sh
npm i
npm start
```
The dev-server starts on [http://localhost:3000](http://localhost:3000)

## server - DjangoRestFramework

### Run dev-server for the first time: 

1. Run docker container with postgres-database
```
docker-compose up -d
```

2. Install dependencies
> Into __server__ dir run following commands
```sh
python3 -m venv .venv
source .venv/bin/activate
.venv/bin/pip install -r r.txt

python manage.py migrate
```

3. Create super user
```sh
python manage.py createsuperuser
```

4. Run dev-server
```sh
python manage.py runserver
```

### Soon to start server run following commands into __server__ dir:
```sh
python3 -m venv .venv
source .venv/bin/activate
python manage.py runserver
```

The dev-server starts on:  [http://localhost:8000](http://localhost:8000)

### Enabled endpoints
- admin/ - admin-panel for manage models & users & auth-tokens
- api/registration/ - user registration
- api/login/ - user auth
- api/answer/ - get answer from model into chatbot

Look up API parametrs see:
- swagger/ - interactive API docs with Swagger-UI
- redoc/ - interactive API docs with ReDoc

### For testing
```sh
curl -u 'admin:admin' \
    -H "Content-Type: application/json" \
    -X POST \
    -d '{"gender":"xyz","age":54}' \
    http://localhost:8000/api/answer/
```
## model - PyTorch Model
The NBO LLM (Russian lang)
