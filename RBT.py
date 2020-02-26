# -*- coding: utf-8 -*-

import time
from selenium import webdriver


def test_1():
    # Инициализация браузера
    browser = webdriver.Chrome()

    # Переходим в поисковик
    browser.get('https://www.google.com/')
    # Ищем поле ввода
    input = browser.find_element_by_css_selector('input[class="gLFyf gsfi"]')
    # Вводим поисковый запрос
    input.send_keys('habrahabr\n')
    # Ждем 1 сек пока поисковая выдача сформируется
    time.sleep(1)
    # Ищем в поисковой выдаче результат со ссылкой на ресурс  habr
    habr_link = browser.find_element_by_css_selector('a[href="https://habr.com/"]')
    # Кликаем по результату выдачи для перехода на сайт
    habr_link.click()
    # Ищем пагинатор
    page = browser.find_element_by_xpath('//a[.="2"]')
    # Кликаем на элемент с указанием второй страницы
    page.click()
    # Сохраняем значение первой статьи на второй странице
    title = browser.find_element_by_css_selector(".post__title_link").text

    # Выведем найденный заголовок
    print(title)

    # Переходим в поисковик
    browser.get('https://www.google.com/')
    # Ищем поле ввода
    input = browser.find_element_by_css_selector('input[class="gLFyf gsfi"]')
    # Вводим в поле ввода заголовок статьи
    input.send_keys(title+'\n')
    # Ждем 1 сек пока поисковая выдача сформируется
    time.sleep(1)
    # Ищем в результатах поисковой выдачи ссылки, содержащие заголовок статьи
    search_resald = browser.find_elements_by_xpath("//h3[text()[contains(.,'" + title + "')]]")

    # Если в результатах присутсвует хотя бы одна статья считаем тест пройденным успешно
    if len(search_resald)>1:
        print('Winner')
    else:
        print('Loser')

    # Закрываем браузер
    browser.close()