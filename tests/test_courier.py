import allure
import pytest
import requests

from tools import RegistrationDate as reg
from data import *


class TestCourier:

    @allure.title('Создание курьера, ожидаем успех.')
    def test_create_new_courier(self):
        response = requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', json=reg.registration_correct_courier())
        assert response.status_code == 201 and response.text == ResponseText.CREATE_COURIER

    @allure.title('Нельзя создать двух одинаковых курьеров, ожидаем ошибку.')
    def test_create_courier_with_registered_login(self):
        response = requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', json=Users.precreated)
        assert response.status_code == 409 and ResponseText.REPETITIVE_COURIER in response.text

    @allure.title('Нельзя создать курьера без пароля, ожидаем ошибку.')
    def test_create_courier_without_password(self):
        response = requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', json=reg.registration_courier_without_password())
        assert response.status_code == 400 and ResponseText.NOT_ENOUGH_REG_DATA in response.text

    @allure.title('Нельзя создать курьера без логина, ожидаем ошибку.')
    def test_create_courier_without_login(self):
        response = requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', json=reg.registration_courier_without_login())
        assert response.status_code == 400 and ResponseText.NOT_ENOUGH_REG_DATA in response.text

    @allure.title('Курьер может авторизоваться, ожидаем успех.')
    def test_login_courier_successful(self):
        response = requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}', json=Users.precreated_login)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Нельзя авторизоваться без пароля или логина, ожидаем ошибку.')
    @pytest.mark.parametrize('without_log_or_pswd', [Users.without_pswd, Users.without_login])
    def test_login_without_all_data(self, without_log_or_pswd):
        response = requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}', json=without_log_or_pswd)
        assert response.status_code == 400 and ResponseText.NOT_ENOUGH_LOG_DATA in response.text

    @allure.title('Нельзя авторизоваться с неверным паролем или логином, ожидаем ошибку.')
    def test_login_with_incorrect_data(self):
        response = requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}', json=Users.incorrect_data)
        assert response.status_code == 404 and ResponseText.INCORRECT_LOG_DATA in response.text
