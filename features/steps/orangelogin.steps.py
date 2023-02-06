from behave import *
from selenium import webdriver


@given(u'I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Firefox()


@when(u'I open homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when(u'I enter username "admin" and password "admin123"')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    context.driver.find_element_by_xpath("//input[@name='password']").send_keys("admin123")


@when(u'I click on login button')
def step_impl(context):
    context.driver.find_element_by_xpath("//button[@type='submit']").click()


@then(u'User must successfully login to dashboard')
def step_impl(context):
    text = context.driver.find_element_by_xpath("h6").text()
    assert text == "Dashboard"
