# Описание

Разработан сайт для федеральной розничной сети магазинов детских игрушек, которая насчитывает 23 магазина по России — от Санкт-Петербурга до Владивостока.

# Реализовано

- регистрация\авторизация;
- корзина, через сессии;
- заказы;
- асинхронные задачи с Celery, Rabbitmq;
- подключен тестовый платежный шлюз;
- экспорт заказов в CSV файл;
- генерация счетов заказов в PDF;
- система купонов (скидка);
- рекомендации по товарам, основанные на предыдущих покупках.

Стек:
- Django
- Braintree
- Celery
- django-ckeditor
- django-crispy-forms
- eventlet
- flower
- Pillow
- requests
- Redis
- pdfkit






<br>
<br>
<br>
<br>

##### Запуск Redis

Для запуска Redis на Windows необходимо запустить дистрибутив Линукса через cmd:
`wsl -d Ubuntu`
Пароль в Убунту стандартный для ПК.

Потом в Убунту запускаем сервер Redis:
`sudo service redis-server start`
<br>
<br>



##### Запуск Celery 

Celery 4.0+ does not officially support window already.
Use `eventlet` instead as below:

`pip install eventlet`

`celery -A <module> worker -l info -P eventlet`

`celery -A conf worker -P eventlet`

##### Запуск Flower

`celery -A conf flower`


<br>
<br>
<br>

###### Проблемы
1) Worker уходит в оффлайн, половина задач не выполняется.
2) PDF сохраняется в корне проекта, браузер создает пустой файл с таким же названием в папке Загрузки.
3) В GetProduct необходимо передать slag, или же получить сразу объект запроса.


###### Задачи
1) Отзывы
2) ЛК с историей заказов, заполненной формой и банковской картой