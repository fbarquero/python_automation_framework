__author__ = 'Mordigan'
from selenium import webdriver
#from page_objects.DaemonProcessesDownPortlet import DaemonProcessesDownPortlet
from driver_factory.driver_factory import DriverManager
from page_objects.Dashboard import DashboardPage

class LoginPage():
    def __init__(self, browser):
        self.driver = DriverManager.new_driver_instance(browser)
        self.driver.get("https://zenoss5x.ip-10-111-2-67.com")

    def check_page(self, title):
        if title in self.driver.title:
            return True

    def insert_credentials(self, username, password):
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("passwrd").clear()
        self.driver.find_element_by_id("passwrd").send_keys("meds22")

    def click_on_login(self):
        self.driver.find_element_by_name("submitbutton").click()
        #daemon_processes_down_portlet =
        return DashboardPage("firefox")


