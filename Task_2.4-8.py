from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # ждем пока цена упадет до 100 долларов
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    print(1) # маркер отладки
    # жждем пока кнопка станет кликаельной
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "book")))
    print(2)
    button.click()
    print(3)
    print(browser.find_element_by_id("input_value").text) # маркер отладки - выводит аргумент функции
    x=int(browser.find_element_by_id("input_value").text) # x - аргумент функции math.log(abs(12*math.sin(int(x))))
    y=str(math.log(abs(12*math.sin(int(x)))))
    # записываем значение y в поле ввода с id = answer
    browser.find_element_by_id("answer").send_keys(str(y))
    # жмем кнопку Submit
    button2 = browser.find_element_by_id("solve")
    button2.click()


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



