import pytest
from data import Data as a
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(autouse=True)
def web_driver():
    s = Service(executable_path='../chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru')
    yield driver
    driver.close()
    driver.quit()

def test_authorization_number(web_driver):
    """ Авторизация по телефону """
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.ID, 't-btn-tab-phone').click()
    time.sleep(1)
    web_driver.find_element(By.ID, 'username').send_keys(a.number)
    web_driver.find_element(By.ID, 'password').send_keys(a.password)
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(web_driver, 3).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h3'))
    )
    assert web_driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"

def test_authorization_login(web_driver):
    """ Авторизация по логину """
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(1)
    web_driver.find_element(By.ID, 'username').send_keys(a.login)
    web_driver.find_element(By.ID, 'password').send_keys(a.password)
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(web_driver, 3).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h3'))
    )
    assert web_driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"

def test_authorization_email(web_driver):
    """ Авторизация по почте """
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.ID, 't-btn-tab-mail').click()
    time.sleep(1)
    web_driver.find_element(By.ID, 'username').send_keys(a.email)
    web_driver.find_element(By.ID, 'password').send_keys(a.password)
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(web_driver, 3).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h3'))
    )
    assert web_driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"

def test_authorization_ls(web_driver):
    """ Авторизация по лицевому счету """
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.ID, 't-btn-tab-ls').click()
    time.sleep(1)
    web_driver.find_element(By.ID, 'username').send_keys(a.account)
    web_driver.find_element(By.ID, 'password').send_keys(a.password)
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(web_driver, 3).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h3'))
    )
    assert web_driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"

def test_negative_authorization_email(web_driver):
    """ Авторизация по телефону в поле аутентификации по почте """
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.ID, 't-btn-tab-mail').click()
    time.sleep(1)
    web_driver.find_element(By.ID, 'username').send_keys(a.number)
    web_driver.find_element(By.ID, 'password').send_keys(a.password)
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(web_driver, 3).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h3'))
    )
    assert web_driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"

def test_negative_authorization_login(web_driver):
    """ Авторизация по телефону в поле аутентификации по логину """
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(1)
    web_driver.find_element(By.ID, 'username').send_keys(a.number)
    web_driver.find_element(By.ID, 'password').send_keys(a.password)
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(web_driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h3'))
    )
    assert web_driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"

def test_negative_authorization_ls(web_driver):
    """ Авторизация по телефону в поле аутентификации по лицевому счету """
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.ID, 't-btn-tab-ls').click()
    time.sleep(1)
    web_driver.find_element(By.ID, 'username').send_keys(a.number)
    web_driver.find_element(By.ID, 'password').send_keys(a.password)
    WebDriverWait(web_driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        'span[class="rt-input-container__meta rt-input-container__meta--error"]'))
    )
    assert (web_driver.find_element(By.CSS_SELECTOR,
            'span[class="rt-input-container__meta rt-input-container__meta--error"]')
            .text == "Проверьте, пожалуйста, номер лицевого счета")

def test_authorization_incorrect_password(web_driver):
    """ Авторизация по логину с некорректным паролем """
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(1)
    web_driver.find_element(By.ID, 'username').send_keys(a.login)
    web_driver.find_element(By.ID, 'password').send_keys(a.incorrect_pass)
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(web_driver, 3).until(
        EC.presence_of_element_located((By.ID, 'form-error-message'))
    )
    assert web_driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_authorization_incorrect_login(web_driver):
    """ Авторизация по некоректному логину """
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(1)
    web_driver.find_element(By.ID, 'username').send_keys(a.incorrect_log)
    web_driver.find_element(By.ID, 'password').send_keys(a.password)
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(web_driver, 3).until(
        EC.presence_of_element_located((By.ID, 'form-error-message'))
    )
    assert web_driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_authorization_without_password(web_driver):
    """ Авторизация по логину без ввода пароля """
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(1)
    web_driver.find_element(By.ID, 'username').send_keys(a.login)
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    try:
        WebDriverWait(web_driver, 3).until(
            EC.presence_of_element_located((By.ID, 'form-error-message'))
        )
        assert web_driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"
    except Exception as ex:
        print(ex)
        print("""Сообщение "Введите пароль, указанный при регистрации" не вывелось!""")

def test_authorization_without_login_and_password(web_driver):
    """ Попытка авторизоваться не вводя логин и пароль """
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(1)
    enter = web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    enter.send_keys(Keys.ENTER)
    time.sleep(1)
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    try:
        WebDriverWait(web_driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'span[class="rt-input-container__meta rt-input-container__meta--error"]'))
        )
        assert (web_driver.find_element(By.CSS_SELECTOR,
                                        'span[class="rt-input-container__meta rt-input-container__meta--error"]')
                .text == "Введите логин, указанный при регистрации")
    except Exception as ex:
        print(ex)
        print("""Сообщение "Введите логин, указанный при регистрации" не вывелось!""")
    try:
        WebDriverWait(web_driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'span[class="rt-input-container__meta rt-input-container__meta--error"]'))
        )
        assert (web_driver.find_element(By.CSS_SELECTOR,
                                        'span[class="rt-input-container__meta rt-input-container__meta--error"]')
                .text == "Введите пароль, указанный при регистрации")
    except Exception as ex:
        print(ex)
        print("""Сообщение "Введите пароль, указанный при регистрации" не вывелось!""")

def test_negative_password_recovery(web_driver):
    """ Пользователь забыл ввести символы с капчи при восстановлении пароля по почте """
    web_driver.implicitly_wait(10)
    web_driver.find_element(By.ID, 'forgot_password').click()
    time.sleep(1)
    web_driver.find_element(By.ID, 't-btn-tab-mail').click()
    time.sleep(1)
    web_driver.find_element(By.ID, 'username').send_keys(a.email)
    time.sleep(1)
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(web_driver, 3).until(
        EC.presence_of_element_located((By.ID, 'form-error-message'))
    )
    assert web_driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или текст с картинки"
