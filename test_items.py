import pytest
from selenium import webdriver

class TestPage():
    def test_answer(self,browser):
        time.sleep(30)
        url="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        browser.get(url)
        button=browser.find_element_by_css_selector('button.btn-add-to-basket')
        assert button is not None     
        
