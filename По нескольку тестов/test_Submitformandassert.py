from selenium import webdriver
import time
import unittest


class test_submit1(unittest.TestCase):
    def test1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

        # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector(
                "div.first_block  > .form-group.first_class > .form-control")
            input1.send_keys("Roman")
            time.sleep(1)
            input2 = browser.find_element_by_css_selector(
                "div.first_block  > .form-group.second_class > .form-control")
            input2.send_keys("Fedyunin")
            time.sleep(1)
            input1 = browser.find_element_by_class_name("form-control.third")
            input1.send_keys("mail@mail.com")
            time.sleep(1)

        # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(2)

        # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(
                "Congratulations! You have successfully registered!", welcome_text)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
        # закрываем браузер после всех манипуляций
            browser.quit()


class test_submit2(unittest.TestCase):
    def test2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

        # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_css_selector(
                "div.first_block  > .form-group.first_class > .form-control")
            input1.send_keys("Roman")
            time.sleep(1)
            input2 = browser.find_element_by_css_selector(
                "div.first_block  > .form-group.second_class > .form-control")
            input2.send_keys("Fedyunin")
            time.sleep(1)
            input1 = browser.find_element_by_class_name("form-control.third")
            input1.send_keys("mail@mail.com")
            time.sleep(1)

        # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(2)

        # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!",
                             welcome_text, "Не получилось заполнить форму")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
        # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == "__main__":
    unittest.main()
