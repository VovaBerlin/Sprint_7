import json
import allure
import pytest
import requests

from data import *


class TestOrders:
    @pytest.mark.parametrize('order_data',
                             [{'color': ['BLACK']}, {'color': ['GREY']}, {'color': ['BLACK', 'GRAY']}, {'color': ['']}])
    @allure.title('Создание заказа, ожидаем успех.')
    def test_create_order_successful(self, order_data):
        Orders.order_data.update(order_data)
        payload_order_data = json.dumps(order_data)
        response = requests.post(f'{Urls.URL}{Handle.CREATE_ORDER}', data=payload_order_data)
        assert response.status_code == 201 and ResponseText.CREATE_ORDER in response.text

    @allure.title('Получить список заказов, ожидаем успех.')
    def test_get_order_list_successful(self):
        response = requests.get(f'{Urls.URL}{Handle.CREATE_ORDER}')
        assert response.status_code == 200 and "orders" in response.json()
