from selenium import webdriver
import time
import math
# import math добавляем чтобы считать ниже формулу (как я понимаю)

link = "http://suninjuly.github.io/find_link_text"
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

def simple_function():
    x = 2+3

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element_by_link_text(link_text).click()
#ссылка зашифрована номером, считается по формуле выше. click - нажимаем на ссылку.

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(40)
    # закрываем браузер после всех манипуляций
    browser.quit()

# какое-то изменение 2

