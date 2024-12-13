import pytest
import allure
from selenium.webdriver import Keys, ActionChains
from pages.home_page import YaScooterHomePage
from utils.test_data import YaScooterHomePageFAQ
from utils.locators import YaScooterHomePageLocator


@allure.epic('Обработка заказов самокатов')
@allure.parent_suite('Домашняя страница')
@allure.suite('Блок "Вопросы о важном"')
class TestYaScooterFAQPage:
    @allure.feature('Аккордеон с вопрос/ответ на домашней странице')
    @allure.story('Блок "Вопросы о важном"')
    @allure.title('При нажатии на вопрос раскрывается ответ ')
    @allure.description('Проверяем, что при нажатии на стрелочку, в блоке "Вопросы о важном",'
                        'открывается соответствующий текст.')
    @pytest.mark.parametrize(
        "question,answer,expected_answer",
        [
            (0, 0, YaScooterHomePageFAQ.answer1),
            (1, 1, YaScooterHomePageFAQ.answer2),
            (2, 2, YaScooterHomePageFAQ.answer3),
            (3, 3, YaScooterHomePageFAQ.answer4),
            (4, 4, YaScooterHomePageFAQ.answer5),
            (5, 5, YaScooterHomePageFAQ.answer6),
            (6, 6, YaScooterHomePageFAQ.answer7),
            (7, 7, YaScooterHomePageFAQ.answer8),
        ]
    )
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.END).key_up(Keys.SHIFT).key_up(Keys.END).perform()
        ya_scooter_home_page.click_faq_question(question_number=question)
        answer = ya_scooter_home_page.find_element(YaScooterHomePageLocator.faq_answer(answer_number=answer))
        assert answer.text == expected_answer, 'Ответ отличается от ожидаемого'
