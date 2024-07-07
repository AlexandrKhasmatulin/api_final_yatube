# Описание

Форум, где можно постить посты и комментировать ~~комментарии~~ посты, а также, конечно, группировать группы и подписывать подписки

API для управления:
- постами (просмотр, создание, обновление, удаление)
- комментариями (просмотр, создание, обновление, удаление)
- сообществами (просмотр)
- подписками (просмотр, создание)

Стек:<br>
Python 3.9: Django 3.2, DRF<br>
SQLite<br>

# Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Kasylin/api_final_yatube.git
```

```
cd api_final_yatube/yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

# Примеры запросов к API

## Получение токена
Запрос:
```
POST api/v1/jwt/create/ HTTP/1.1
content-type: application/json

{
    "username": "string",
    "password": "string"
}
```
Пример ответа:
```
{
  "refresh": "string",
  "access": "string"
}
```

## Просмотр списка публикаций
Запрос:
```
GET api/v1/posts/?limit=1&offset=1 HTTP/1.1
Authorization: Bearer [token]
content-type: application/json
```
Пример ответа:
```
{
    "count": 11,
    "next": "/api/v1/posts/?limit=1&offset=2",
    "previous": "/api/v1/posts/?limit=1",
    "results": [
        {
            "id": 2,
            "author": "regular_user",
            "text": "Пост зарегистрированного пользователя.",
            "pub_date": "2023-11-30T10:03:46.978297Z",
            "image": null,
            "group": null
        }
    ]
}
```

## Создание комментария
Запрос:
```
POST api/v1/posts/1/comments/ HTTP/1.1
Authorization: Bearer [token]
content-type: application/json

{
    "text": "Тестовый комментарий"
}
```
Пример ответа:
```
{
    "id": 16,
    "author": "regular_user",
    "text": "Тестовый комментарий",
    "created": "2023-11-30T17:56:36.441500Z",
    "post": 1
}
```

## Просмотр информации о сообществе
Запрос:
```
GET api/v1/groups/1/ HTTP/1.1
Authorization: Bearer [token]
content-type: application/json
```
Пример ответа:
```
{
    "id": 1,
    "title": "TestGroup",
    "slug": "test-group",
    "description": "Some text."
}
```

## Оформление подписки
Запрос:
```
POST /api/v1/follow/ HTTP/1.1
Authorization: Bearer [token]
content-type: application/json

{
    "following": "root"
}
```
Пример ответа:
```
{
  "user": "testuser",
  "following": "root"
}
```
author: Alex