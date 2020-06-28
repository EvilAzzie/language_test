import pytest
import time
import math
from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

class TestPage():

    @pytest.mark.parametrize('url',["https://stepik.org/lesson/236895/step/1",
                                    "https://stepik.org/lesson/236896/step/1",
                                    "https://stepik.org/lesson/236897/step/1",
                                    "https://stepik.org/lesson/236898/step/1",
                                    "https://stepik.org/lesson/236899/step/1",
                                    "https://stepik.org/lesson/236903/step/1",
                                    "https://stepik.org/lesson/236904/step/1",
                                    "https://stepik.org/lesson/236905/step/1"])
    def test_answer(self,browser,url):
        browser.get(url)
        answer = math.log(int(time.time()+2))
        txtarea=browser.find_element_by_css_selector('textarea[class="textarea string-quiz__textarea ember-text-area ember-view"]')
        txtarea.send_keys(str(answer))
        button=browser.find_element_by_css_selector('button[class="submit-submission"]')
        button.click()
        btn=browser.find_element_by_css_selector('pre[class="smart-hints__hint"]')
        btntxt=btn.text
        print(btntxt)
        assert btntxt=="Correct!"     
        
