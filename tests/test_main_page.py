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
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, 'username').send_keys(a.login)
    driver.find_element(By.ID, 'password').send_keys(a.password)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_main_header(web_driver):
    """ Просмотр основных страниц в главной шапке сайта """
    web_driver.find_element(By.ID, 'id_app_lk_b2c').click()
    time.sleep(5)
    web_driver.find_element(By.XPATH, '//div[@class="StyledBottomLinksWrapper-YYdXz bbsGQi"]/div[2]/p').click()
    time.sleep(3)
    web_driver.find_element(By.XPATH, '//div[@class="application-header_bottom_navigation"]/a[3]').click()
    time.sleep(3)
    web_driver.find_element(By.XPATH, '//div[@class="StyledBottomLinksWrapper-YYdXz bbsGQi"]/div[4]/p').click()
    time.sleep(3)
    web_driver.find_element(By.XPATH, '//div[@class="application-header_bottom_navigation"]/a[5]').click()
    time.sleep(3)
    web_driver.find_element(By.XPATH, '//div[@class="StyledBottomLinksWrapper-YYdXz bbsGQi"]/div[6]/p').click()
    time.sleep(3)
    web_driver.find_element(By.XPATH, '//div[@class="application-header_bottom_navigation"]/a[7]').click()
    time.sleep(5)
    print("SUPERRR!!!")

def test_profile_in_footer(web_driver):
    """ Поиск ссылки на профиль в футере и сверка данных """
    web_driver.find_element(By.ID, 'id_app_lk_b2c').click()
    web_driver.implicitly_wait(10)
    web_driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    web_driver.find_element(By.XPATH,
                            '//div[@class="StyledFooterContentBlockDesktop-TzaNz gmVttF"]'
                            '/div[3]/div[1]/p').click()
    web_driver.refresh()
    time.sleep(5)
    WebDriverWait(web_driver, 3).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@class="n-section profile_section_rtkid padding-l white border-no"]/div[5]/div[2]'))
    )
    assert (web_driver.find_element
            (By.XPATH, '//div[@class="n-section profile_section_rtkid padding-l white border-no"]/div[5]/div[2]')
            .text == a.login)

def test_personal_accounts(web_driver):
    """ Управление лицевым счетом и просмотр документов """
    web_driver.find_element(By.ID, 'id_app_lk_b2c').click()
    web_driver.implicitly_wait(10)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div.StyledAccountsWidgetServicesBrief-ikqhgq.VsMbv > button > span').click()
    web_driver.implicitly_wait(10)
    web_driver.find_element(By.CSS_SELECTOR, 'div.account-header_name > nobr')
    assert (web_driver.find_element(By.CSS_SELECTOR, 'div.account-header_name > nobr').text == a.account)
    time.sleep(5)
    web_driver.find_element(By.LINK_TEXT, "Главная").click()
    web_driver.implicitly_wait(10)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div.StyledEntryPageLeftPart-goVwnv.iYgrwF > div > div:nth-child(3) > div').click()
    time.sleep(5)
    web_driver.find_element(By.CSS_SELECTOR, 'div.FuncButton-bOtxHL.fMugMP.Button-dtEEMF.igzCon > div').click()
    print('DAS IST GUT!')

def test_help(web_driver):
    """ Помошь по ключевому слову "Тарифы" """
    web_driver.find_element(By.ID, 'id_app_lk_b2c').click()
    web_driver.implicitly_wait(10)
    web_driver.find_element(By.XPATH, '//div[@class="StyledHeaderTopPartMenu-cvptKI hPDveJ"]'
                                      '/div[2]/div[1]').click()
    web_driver.implicitly_wait(10)
    field = web_driver.find_element(By.CLASS_NAME, 'rtk-help-search-content-input-field')
    field.send_keys('Тарифы')
    time.sleep(1)
    field.send_keys(Keys.ARROW_DOWN)
    field.send_keys(Keys.ARROW_DOWN)
    field.send_keys(Keys.ENTER)
    field.send_keys(Keys.ENTER)
    time.sleep(3)
    WebDriverWait(web_driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h3'))
    )
    assert web_driver.find_element(By.TAG_NAME, 'h3').text == "Результаты поиска"

def test_footer_desktop(web_driver):
    """ Проверка некоторых ссылок в футере на главной странице """
    web_driver.find_element(By.ID, 'id_app_lk_b2c').click()
    web_driver.implicitly_wait(10)
    web_driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    (web_driver.find_element
     (By.CSS_SELECTOR, 'div.StyledFooterContentBlockDesktop-TzaNz.gmVttF > div:nth-child(2)'
                       ' > div:nth-child(1)').click())
    time.sleep(5)
    web_driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    (web_driver.find_element
     (By.CSS_SELECTOR, 'div.StyledFooterContentBlockDesktop-TzaNz.gmVttF > div:nth-child(2)'
                       ' > div:nth-child(2)').click())
    time.sleep(5)
    web_driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    (web_driver.find_element
     (By.CSS_SELECTOR, 'div.application-footer_navigation-group.application-footer_navigation-group_1'
                       ' > a:nth-child(3) > span').click())
    time.sleep(5)
    web_driver.find_element(By.LINK_TEXT, "Главная").click()
    web_driver.implicitly_wait(10)
    web_driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    (web_driver.find_element
     (By.CSS_SELECTOR, 'div.StyledFooterContentBlockDesktop-TzaNz.gmVttF > div:nth-child(2)'
                       ' > div:nth-child(4)').click())
    time.sleep(5)

def test_cctv(web_driver):
    """ Тест страницы с информацией об видеонаблюдениии """
    web_driver.find_element(By.ID, 'rt-btn').click()
    web_driver.implicitly_wait(10)
    web_driver.find_element(By.CSS_SELECTOR, 'div.main-nav.rtk-tabs > div > div:nth-child(4) > div').click()
    web_driver.implicitly_wait(10)
    web_driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    web_driver.find_element(By.CSS_SELECTOR,
                            'div:nth-child(1) > button > div[class="d-flex align-center"]').click()
    time.sleep(1)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div:nth-child(2) > button > div[class="d-flex align-center"]').click()
    time.sleep(1)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div:nth-child(3) > button > div[class="d-flex align-center"]').click()
    time.sleep(1)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div:nth-child(4) > button > div[class="d-flex align-center"]').click()
    time.sleep(1)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div:nth-child(5) > button > div[class="d-flex align-center"]').click()
    time.sleep(1)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div:nth-child(6) > button > div[class="d-flex align-center"]').click()
    time.sleep(1)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div:nth-child(7) > button > div[class="d-flex align-center"]').click()
    time.sleep(1)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div:nth-child(8) > button > div[class="d-flex align-center"]').click()
    time.sleep(1)
    print("Никого не потеряли!")

def test_social_media(web_driver):
    """ Переход по ссылкам на социальные сети компании """
    web_driver.find_element(By.ID, 'rt-btn').click()
    time.sleep(2)
    web_driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    web_driver.implicitly_wait(10)
    web_driver.find_element(By.CSS_SELECTOR, 'a[href="/help#contacts"]').click()
    web_driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div[class="d-flex classIconBox"] > a:nth-child(1) > svg').click()
    time.sleep(5)
    web_driver.switch_to.window(web_driver.window_handles[0])
    web_driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div[class="d-flex classIconBox"] > a:nth-child(2) > svg').click()
    time.sleep(5)
    web_driver.switch_to.window(web_driver.window_handles[0])
    web_driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    web_driver.implicitly_wait(5)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div[class="d-flex classIconBox"] > a:nth-child(3) > svg').click()
    time.sleep(5)
    web_driver.switch_to.window(web_driver.window_handles[0])

def test_list_of_tariffs(web_driver):
    """ Просмотр списка тарифов """
    web_driver.find_element(By.ID, 'rt-btn').click()
    web_driver.implicitly_wait(10)
    web_driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    web_driver.find_element(By.CSS_SELECTOR,
                            'div[class="rt-tabs-v2-navigation"] > div:nth-child(1)').click()
    assert web_driver.find_element(By.CSS_SELECTOR,
                                   'div[class="rt-tabs-v2-navigation"]'
                                   ' > div:nth-child(1) > button').text == 'Домашний интернет'
    time.sleep(3)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div[class="rt-tabs-v2-navigation"] > div:nth-child(2)').click()
    assert web_driver.find_element(By.CSS_SELECTOR,
                                   'div[class="rt-tabs-v2-navigation"]'
                                   ' > div:nth-child(2) > button').text == 'с телевидением'
    time.sleep(3)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div[class="rt-tabs-v2-navigation"] > div:nth-child(3)').click()
    assert web_driver.find_element(By.CSS_SELECTOR,
                                   'div[class="rt-tabs-v2-navigation"]'
                                   ' > div:nth-child(3) > button').text == 'с ТВ и мобильной связью'
    time.sleep(3)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div[class="rt-tabs-v2-navigation"] > div:nth-child(4)').click()
    assert web_driver.find_element(By.CSS_SELECTOR,
                                   'div[class="rt-tabs-v2-navigation"]'
                                   ' > div:nth-child(4) > button').text == 'с мобильной связью'
    time.sleep(3)
    web_driver.find_element(By.CSS_SELECTOR,
                            'div[class="rt-tabs-v2-navigation"] > div:nth-child(5)').click()
    assert web_driver.find_element(By.CSS_SELECTOR,
                                   'div[class="rt-tabs-v2-navigation"]'
                                   ' > div:nth-child(5) > button').text == 'с видеонаблюдением'
    time.sleep(3)
    print("ВСЕ НА МЕСТЕ!!!")
