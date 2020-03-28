import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_FindButtonBasket(browser):
    try:
        browser.get(link)
        
        time.sleep(30)
        button = browser.find_element_by_css_selector("button.btn-add-to-basket")
        result = True
    except:
        result = False
    assert result == True, '!!!!!!! Не нашёл кнопку "Добавить в карзину"!!!!!!!'
    
