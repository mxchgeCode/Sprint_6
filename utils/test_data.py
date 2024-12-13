from faker_e164.providers import E164Provider
from faker import Faker


class YaScooterHomePageFAQ:
    answer1 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    answer2 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    answer3 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    answer4 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    answer5 = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    answer6 = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    answer7 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    answer8 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."


class YaScooterOrderPageData:
    fake = Faker("ru_RU")
    fake.add_provider(E164Provider)
    data_sets = {
        'data_set1': {
            'first_name': fake.first_name_male(),
            'last_name': fake.last_name_male(),
            'address': fake.street_name(),
            'subway_name': 'Беговая',
            'telephone_number': fake.safe_e164(region_code="US"),
            'date': fake.date('%d.%m.%Y'),
            'rental_period': 0,
            'color': [0],
            'comment_for_courier': fake.words()
        },
        'data_set2':
            {
             'first_name': fake.first_name_male(),
             'last_name': fake.last_name_male(),
             'address': fake.street_name(),
             'subway_name': 'Комсомольская',
             'telephone_number': fake.safe_e164(region_code="US"),
             'date': fake.date('%d.%m.%Y'),
             'rental_period': 1,
             'color': [0, 1],
             'comment_for_courier': fake.words()
             },
    }
