__author__ = 'Mordigan'
from driver_factory.driver_factory import DriverManager
class DaemonProcessesDownPortlet():
    def __init__(self):
        self.driver = DriverManager.get_driver_instance()

    def is_portlet_displayed(self):
        try:
            element = self.driver.find_element_by_xpath("//div[@class='portlet-header']//div[starts-with(@id,'heartbeats')]")
            return True
        except Exception:
            return False
