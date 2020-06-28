import pytest
import time
from selenium import webdriver


class TestPage():
    def test_answer(self,browser):
        url="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(url)
        button=None
        try:
            button=browser.find_element_by_css_selector('button.btn-add-to-basket')
        except:
            pass            
        time.sleep(10)
        assert button is not None, "button not found"    
        
