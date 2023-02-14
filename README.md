# stripe_api
## Описание
Пример реализации добавления платежной системы stripe.
Реализованы view функции для генерации checkout session и отображения страницы товара.

## Установка
```
git clone https://github.com/danyadanyaa/stripe_api.git
```
```
cd stripe_api/docker-compose
```

#### Создайте файл .env в директории docker-compose/ и добавьте переменные окружения:
```
DJANGO_SECRET_KEY='Секретный ключ Django'
STRIPE_PUBLISHABLE_KEY='Публичный ключ stripe'
STRIPE_SECRET_KEY='Секретный ключ stripe'
DB_ENGINE = engine дб
DB_NAME = имя Вашей дб
POSTGRES_USER = имя юзера дб
POSTGRES_PASSWORD = ваш пароль для пользования 
DB_HOST = хост для базы данных
DB_PORT = порт для базы данных
SITE_URL='Адрес сайта (http://127.0.0.1/ при запуске локально)'
```
#### Запустите сборку контейнеров docker командой:
```
docker compose up -d --build
```

#### Выполните миграции:
```
docker-compose exec web python manage.py migrate
```
#### Скопируйте файлы статики в контейнер:
```
docker-compose exec web python manage.py collectstatic --no-input
```
#### При необходимости создайте профиль администратора:
```
docker-compose exec web python manage.py createsuperuser
```
#### Выполните импорт данных в базу данных:
```
docker-compose exec web python manage.py loaddata fistures.json
```
