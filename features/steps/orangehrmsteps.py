from behave import *
from selenium import webdriver



@given(u'launch browser')
def launchbrowser(context):
  context.driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.32.0-win-aarch64.zip\geckodriver.exe")


@when(u'open orange hrm homepage')
def openhomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then(u'verify that the logo present on page')
def verifylogo(context):

    context.driver.find_element_by_xpath("//div[@class='orangehrm-login-logo']").is_displayed()


@then(u'close browser')
def closebrowser(context):
    context.driver.close()
