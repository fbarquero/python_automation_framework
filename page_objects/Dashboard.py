import time

__author__ = 'Mordigan'
from driver_factory.driver_factory import DriverManager
from page_objects.DaemonProcessesDownPortlet import DaemonProcessesDownPortlet

class DashboardPage():
    def __init__(self, browser):
        self.driver = DriverManager.get_driver_instance()

    def navigate_to(self, page):
        if page is "Dashboard":
            self.driver.find_element_by_id("Dashboard-nav-button")
            return self
        else:
            return False

    def check_page(self, title):
        if title in self.driver.title:
            return True

    '''
        public void clickOnAddPortletLink() {
        Utilities.waitTime(ConstantsClass.TIMEOUT_2_SECONDS);
        WebDriverCommands.click(By.partialLinkText(ADD_PORTLET_LINK), ConstantsClass.TIMEOUT_15_SECONDS);
    }
    '''
    def click_on_add_portlet_link(self):
        self.driver.find_element_by_partial_link_text("Add portlet").click()

    def is_add_portlet_popup_displayed(self):
        time.sleep(10)
        if "Add Portlet" in self.driver.find_element_by_id("addPortletDialog_h").text:
            return True
        else:
            return False

    def add_portlet(self, portlet_name):
        if portlet_name is "daemonportlet":
            self.driver.find_element_by_xpath("//div[@id='addPortletDialog']//button[.='Daemon Processes Down']").click()
            return DaemonProcessesDownPortlet()


