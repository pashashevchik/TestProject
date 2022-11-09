from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """ Open url """
        self.driver.get(self.url)

    #Method get element
    def     get_element(self, locator, timeout=10, select_method="clickable"):
        """ Gets the element  """
        return wait(self.driver, 10).until(EC.element_to_be_clickable((locator)))
        if select_method == "clickable":
            return wait(self.driver, 10).until(EC.element_to_be_clickable((locator)))
        elif select_method == "selected":
            return wait.until(EC.element_to_be_selected((locator)))
        elif select_method == "visibility_located":
            return wait.until(EC.visibility_of_element_located((locator)))
        elif select_method == "visibility_of_all_located":
            return wait.until(EC.visibility_of_all_elements_located((locator)))
        elif select_method == "presence_element":
            return wait.until(EC.presence_of_element_located((locator)))
        elif select_method == "presence_of_all_element":
            return wait.until(EC.presence_of_all_elements_located((locator)))
        elif select_method == "element_not_visible":
            return wait.until(EC.invisibility_of_element_located((locator)))

    #Method go to element
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


