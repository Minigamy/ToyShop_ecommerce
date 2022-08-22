# Запуск Celery 

Celery 4.0+ does not officially support window already.
Use `eventlet` instead as below:

`pip install eventlet`

`celery -A <module> worker -l info -P eventlet`

`celery -A conf worker -P eventlet`

# Запуск Flower

`celery -A conf flower`

# Запуск WeasyPrint
Запуск оболочки MSYS2. В ней  