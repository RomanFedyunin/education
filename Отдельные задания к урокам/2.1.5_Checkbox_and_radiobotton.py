from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    time.sleep(2)

    checkbox = browser.find_element_by_id('robotCheckbox').click()
    time.sleep(2)
    radiobutton = browser.find_element_by_id('robotsRule').click()
    time.sleep(2)
    submit = browser.find_element_by_class_name('btn.btn-default').click()
    time.sleep(2)

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
