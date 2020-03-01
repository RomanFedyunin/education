from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Roman")

    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Fedyunin")

    email = browser.find_element_by_name("email")
    email.send_keys("roma@mail.ru")

    upload_file = browser.find_element_by_name("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'File_for_upload.txt')
    # добавляем к этому пути имя файла
    upload_file.send_keys(file_path)

    submit = browser.find_element_by_class_name("btn.btn-primary").click()


finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(7)
        # закрываем браузер после всех манипуляций
        browser.quit()
