from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "http://suninjuly.github.io/get_attribute.html"
  browser = webdriver.Chrome()
  browser.get(link)

  treasure = browser.find_element_by_id('treasure')
  # Находим элемент по ID
  x_element = treasure.get_attribute('valuex')
  # берём значение из атрибута этого элемента
  x = x_element
  y = calc(x)

  answer = browser.find_element_by_id('answer').send_keys(y)
  time.sleep(1)

  checkbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
  radiobutton = browser.find_element_by_id('robotsRule').click()

  time.sleep(1)

  submit = browser.find_element_by_class_name('btn.btn-default').click()
  time.sleep(1)

finally:
      # ожидание чтобы визуально оценить результаты прохождения скрипта
      time.sleep(10)
      # закрываем браузер после всех манипуляций
      browser.quit()
