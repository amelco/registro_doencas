## Executando a solução

Instalando e iniciando o Postgres
```
$ cd bd
$ docker-compose up -d
$ cd ..
```

Crie um ambiente virtual python e instale as dependências
```
$ cd registro
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Faça as `migrations` do banco de dados:
```
$ python manage.py makemigrations
$ python manage.py migrate
```

Inicialize o servidor:
```
$ python manage.py runserver
```

A página será exibida em `http://127.0.0.1:8000/cadastro/`