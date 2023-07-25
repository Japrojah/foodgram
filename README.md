# Foodrgam
# Для ревью:
- адрес 'https://dima.servepics.com'
  ip '158.160.29.10'
- log/pass 'Dima'/'Dima' - что забавно, ведь я дипломированный специалист по ИБ
## Технологии:
- Python==3.9
- Django==3.2.16
- IncrementalBar
- Docker
- gunicorn==20.0.4
- PyJWT==2.6
- djangorestframework==3.14 

## Реализованы:

- Работа проекта в контейнерах Docker
- Образы backend & frontend приложений доступны в DockerHub по именам japrojah/foodgram_(backend/frontend);
- Вот-вот состоится деплой проекта на сервер.

## Как развернуть проект на локальной машине:

### Установите необходимые инструменты на сервер: docker & docker-compose.
### Создайте файл `/infra/.env` с данными из шаблона `/infra/.env.example`.
### Выполните команду `docker compose up -d --buld`.
### Далее выполните миграции с помощью: `docker compose exec backend python manage.py migrate`.
### Создайте пользователя с правами администратора с помощью: `docker-compose exec backend python manage.py createsuperuser`.
### Соберите статику с помощью: `docker compose exec backend python manage.py collectstatic`.
#### При неоднократном запуске проекта и внесении изменений в конфигурацию кода добавьте к вышеуказанной команде тэг "--no-cache" 
### Запустите загрузку ингредиентов `docker compose exec backend python manage.py load_ingredients`.
#### Вы увидите графическое представление процесса загрузки файлов в окне терминала.
### Не забудьте заранее создать несколько "тегов" через админку - это нужно для корректной работы приложения.
### Документация к API находится по адресу: <http://localhost/api/docs/redoc.html>.
### Сервис будет доступен по адресу "http:/localhost/".
#### Примеры других запросов: 'http:/localhost/recipes/', 'http:/localhost/admin/', 'http:/localhost/users/', 'http:/localhost/tags/', 'http:/localhost/ingredients/'. 
