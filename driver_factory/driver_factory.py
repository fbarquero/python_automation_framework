__author__ = 'GrimReaper'

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

class DriverManager():
    driver = None
    @staticmethod
    def get_driver_instance():
        return DriverManager.driver
        #coment

    @staticmethod
    def new_driver_instance(browser_name):
        if browser_name is "firefox":
            DriverManager.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=DesiredCapabilities.FIREFOX)
        elif browser_name is 'chrome':
            DriverManager.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
        elif browser_name is 'ie':
            DriverManager.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
        DriverManager.driver.implicitly_wait(30)
        DriverManager.driver.maximize_window()
        return DriverManager.driver



