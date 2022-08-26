# Запуск Celery 

Celery 4.0+ does not officially support window already.
Use `eventlet` instead as below:

`pip install eventlet`

`celery -A <module> worker -l info -P eventlet`

`celery -A conf worker -P eventlet`

# Запуск Flower

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