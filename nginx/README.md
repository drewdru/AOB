Настройка
=============================
NGINX
------------
Необходимо изменить настройки ```/nginx/nginx.conf``` под текущую машину


Docker
------------
Необходимо настроить ```docker-compose.yml```

	nginx:
		...
		ports:
  		  - "8000:8000" # Порт для nginx
		environment:
  		  - NGINX_HOST=api.aigeo.ru  адрес сайта
		  - NGINX_PORT=8000  Порт для nginx
	web:
		...
		ports:
		  - "8001:8001" # Порт для uwsgi
		extra_hosts:
		  - "map-db:ВНЕШНИЙ_IP_АДРЕС"

UWSGI
------------
Необходимо настроить ```uwsgi.ini```

	[uwsgi]
	...
	socket = :8001 # Порт для uwsgi
	processes = 3 # количество процессов
	threads = 2 # количество потоков

Клонирование проекта с подмодулями
------------

	git clone git@git.aigeo.ru:aigeo/geoportal.git
	cd geoportal
	git submodule init
	git submodule update


DEPLOY
------------
django wsqi application

