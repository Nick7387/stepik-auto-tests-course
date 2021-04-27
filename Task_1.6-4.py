from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
browser.get(link)

try:
   

    input1 = browser.find_element_by_xpath("//div[@class='container']/form[@action='#']//input[@name='first_name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//div[@class='container']/form[@action='#']//input[@name='last_name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//div[@class='container']/form[@action='#']/div[3]/input[@name='firstname']")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_xpath("/html//input[@id='country']")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла