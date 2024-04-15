import requests
import configuration
from data import user_body

def test_sign_up():
     response = requests.post(configuration.URL_SERVICE + configuration.SIGNUP_PATH, data=user_body)
     assert response.status_code == 200, 'Поля email и password обязательны к заполнению'

def test_sign_in():
    response = requests.post(configuration.URL_SERVICE + configuration.SIGNIN_PATH, data=user_body)
    assert 'Welcome' in response.text, 'Данный пользователь не существует'

def test_logout():
    response = requests.get(configuration.URL_SERVICE + configuration.LOGOUT_PATH)
    assert response.status_code == 200, 'Выход из системы уже осуществлен'

def get_email():
    current_body = user_body.copy()
    current_body['email']=''
    return current_body

def get_password():
    current_body = user_body.copy()
    current_body['password'] = ''
    return current_body

def test_negative_signup_email():
    response = requests.post(configuration.URL_SERVICE + configuration.SIGNUP_PATH, get_email())
    assert response.status_code != 200, 'Приложение принимает пустое значение в поле email при авторизации'

def test_negative_signup_password():
    response = requests.post(configuration.URL_SERVICE + configuration.SIGNIN_PATH, get_password())
    assert response.status_code != 200, 'Приложение принимает пустое значение в поле password при авторизации'

def get_user_body_not_sign_up():
    current_body = user_body.copy()
    current_body['email'] = 'Ivan@mail.ru'
    return current_body

def get_user_body_invalid_password():
    current_body = user_body.copy()
    current_body['password'] = 'Qwerty'
    return current_body

def test_negative_login_email():
    response = requests.post(configuration.URL_SERVICE + configuration.SIGNIN_PATH, get_user_body_not_sign_up())
    assert 'Please check your login details and try again' in response.text, 'Приложение позволяет войти незарегестрированным полльзователям'

def test_negative_login_password():
    response = requests.post(configuration.URL_SERVICE + configuration.SIGNIN_PATH, get_user_body_invalid_password())
    assert 'Please check your login details and try again' in response.text, 'Приложение позволяет войти под любым паролем'