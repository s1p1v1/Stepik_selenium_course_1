import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Задача 1
# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)

    x = int(browser.find_element_by_id("num1").text)
    y = int(browser.find_element_by_id("num2").text)
    sel = Select(browser.find_element_by_class_name("custom-select"))
    sel.select_by_value(str(x + y))

    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

