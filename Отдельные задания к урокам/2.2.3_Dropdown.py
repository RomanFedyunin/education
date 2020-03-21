from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_xpath("//span[@id='num1']").text
    num2 = browser.find_element_by_id('num2').text
    sum = str(int(num1) + int(num2))

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_visible_text(sum)
# Выбираем из списка значение, где текст равен переменной sum

    submit = browser.find_element_by_class_name('btn.btn-default').click()
    time.sleep(1)

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
