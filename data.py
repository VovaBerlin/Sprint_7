class Handle:
    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    CREATE_ORDER = '/api/v1/orders'


class Urls:
    URL = 'http://qa-scooter.praktikum-services.ru'


class ResponseText:
    CREATE_COURIER = '{"ok":true}'
    REPETITIVE_COURIER = 'Этот логин уже используется'
    NOT_ENOUGH_REG_DATA = 'Недостаточно данных для создания учетной записи'
    NOT_ENOUGH_LOG_DATA = 'Недостаточно данных для входа'
    INCORRECT_LOG_DATA = 'Учетная запись не найдена'
    CREATE_ORDER = 'track'


class Users:
    precreated = {
        "login": "test14377",
        "password": "test143772",
        "name": "testtt"
    }
    precreated_login = {
        "login": "test14377",
        "password": "test143772"
    }

    without_pswd = {
        "login": "test14377",
        "password": ""
    }

    without_login = {
        "login": "",
        "password": "test143772"
    }
    incorrect_data = {
        "login": "test143772",
        "password": "test1437723",
        "name": "testtt"
    }


class Orders:
    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-09-22",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
