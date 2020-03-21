from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("trollface.btn.btn-primary").click()
    second_window = browser.window_handles[1]
    # узнаём название новой вкладки (второй по порядку, отсчёт с 0)
    browser.switch_to.window(second_window)
    # переходим на новую вкладку

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)
    input = browser.find_element_by_id('answer').send_keys(y)

    submit = browser.find_element_by_class_name("btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
