"""
https://stepik.org/lesson/237240/step/9?unit=209628
Задание: запуск автотестов для разных языков интерфейса

pytest --language=es test_items.py
pytest --language=fr test_items.py
pytest --language=en-gb test_items.py
"""
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_should_exist(browser):
    browser.get(link)
    time.sleep(7)
    buttons = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert buttons > 0, 'The button "Add to basket" is not found'
