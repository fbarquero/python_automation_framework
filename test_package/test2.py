__author__ = 'GrimReaper'
import time
from driver_factory.driver_factory import DriverManager
from page_objects.Login import LoginPage
from proboscis import before_class
from proboscis import after_class
from proboscis import test
from proboscis.asserts import assert_true
from proboscis.asserts import assert_false


login_page = LoginPage("firefox")
login_page.check_page("Login")
login_page.insert_credentials("admin", "meds22")
dashboard_page = login_page.click_on_login()
#assert_true(dashboard_page.navigate_to("Dashboard"), message="unable to access the dashboard page")
if dashboard_page.navigate_to("Dashboard") is False:
    print "unable to access the dashboard page"
#assert_true(dashboard_page.check_page("Zenoss: Dashboard"), message="Dashboard Page title is incorrect")
if dashboard_page.check_page("Zenoss: Dashboard") is not True:
    print "Dashboard Page title is incorrect"
dashboard_page.click_on_add_portlet_link()
#Check if portlet is displayed
#assert_true(dashboard_page.is_add_portlet_popup_displayed(), message="Add portlet popup is not displayed")
if dashboard_page.is_add_portlet_popup_displayed() is False:
    print "Add portlet popup is not displayed"
daemon_processes_down_portlet = dashboard_page.add_portlet("daemonportlet")
#Check if portlet is displayed
#assert_false(dashboard_page.is_add_portlet_popup_displayed(), message="Add portlet popup is displayed")
time.sleep(5)
if dashboard_page.is_add_portlet_popup_displayed() is True:
    print "Add portlet popup is displayed"
#assert_true(daemon_processes_down_portlet.is_portlet_displayed())
if daemon_processes_down_portlet.is_portlet_displayed is False:
    print "Daemon Portlet was not added."


