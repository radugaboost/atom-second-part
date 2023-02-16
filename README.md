# Как установить
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Как запустить
$ docker-compose build
$ docker-compose up

# После этого пройти по этой ссылке
$ http://localhost:9000/
$ user: admin
$ password: admin
$ http://localhost:9000/d/KvPliOJVk/atom?orgId=1

# .env 
## psql

- DATABASE - имя базы данных.
- DB_USER - имя пользователя.
- DB_PASSWORD - пароль для пользователя .
- DB_HOST - адрес сервера базы данных.
- DB_PORT - порт базы данных.
