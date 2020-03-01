from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:

    link="http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 150)")
# Скролим страницу на 100 пикселей

    input = browser.find_element_by_id('answer').send_keys(y)

    check = browser.find_element_by_id('robotCheckbox').click()
    button = browser.find_element_by_id('robotsRule').click()
    submit = browser.find_element_by_class_name('btn.btn-default').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
