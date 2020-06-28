import pytest
import time
from selenium import webdriver

class TestPage():
    def test_answer(self,browser):
        url="https://readmanga.me/beastars/vol3/17"
        browser.get(url)
        button=browser.find_element_by_css_selector('button.btn-add-to-basket')
        time.sleep(10)
        assert button, "button not found"    
        
