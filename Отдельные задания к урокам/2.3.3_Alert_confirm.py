from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn.btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()
# соглашаемся с сообщением во всплавшем предупреждении

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)
    input = browser.find_element_by_id('answer').send_keys(y)

    submit = browser.find_element_by_class_name("btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
