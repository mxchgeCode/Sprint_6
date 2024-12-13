import allure
from utils.urls import Urls
from pages.home_page import YaScooterHomePage


@allure.epic('Обработка заказов самокатов')
@allure.parent_suite('Домашняя страница')
@allure.story('Переход к странице "Оформление заказа" ')
@allure.suite('Переход к странице "Оформление заказа" по кнопке "Заказать" вверху домашней страницы')
class TestYaScooterHomePage:
    @allure.feature('Фича_Переход к форме "Оформление заказа" из Домашней страницы')
    @allure.story('Стори_Переход к "Оформление заказа" по кнопке "Заказать" из header')
    @allure.title('Нажатие на кнопку "Заказать" вверху страницы.')
    @allure.description('Проверка что при нажатии по кнопке "Заказать", вверху домашней страницы'
                        'происходит корректный переход на страницу "Оформления заказа".')
    def test_click_top_order_button_show_order_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_top_order_button()
        assert ya_scooter_home_page.current_url() == Urls.ORDER_PAGE

    @allure.feature('Переход к форме "Оформление заказа" из Домашней страницы')
    @allure.story('Переход к "Оформление заказа" по кнопке "Заказать" из блока "Как это работает"')
    @allure.title('Нажатие на кнопку "Заказать", в блоке "Как это работает".')
    @allure.description('Проверка что, при нажатии по кнопке "Заказать", в блоке "Как это работает" '
                        'происходит корректный переход на страницу "Оформления заказа".')
    def test_click_bottom_order_button_show_order_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_bottom_order_button()
        assert ya_scooter_home_page.current_url() == Urls.ORDER_PAGE

    @allure.feature('Переход на страницу "ЯндексДзен" из Домашней страницы')
    @allure.story("Редирект на страницу ЯндексДзен по кнопке logo вверху страницы")
    @allure.title('При нажатии на лого "ЯндексСамокат" происходит редирект на страницу "ЯндексДзен"')
    @allure.description('Проверка что при нажатии по кнопке "ЯндексСамокат",вверху домашней страницы'
                        'происходит корректный редирект на страницу "ЯндексДзен".')
    def test_click_yandex_button_go_to_yandex(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_yandex_button()
        ya_scooter_home_page.switch_window(1)
        ya_scooter_home_page.wait_url_until_not_about_blank()
        current_url = ya_scooter_home_page.current_url()

        assert (Urls.YANDEX_HOME_PAGE in current_url) or (Urls.DZEN_HOME_PAGE in current_url) or (
                Urls.YANDEX_CAPTCHA_PAGE in current_url)
