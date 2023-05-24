from behave import given
from behave import when
from behave import then
from PageFactory import HRMPage

@given(u'I am able to open the browser and open the url')
def step_impl(context):
    HRMPage.launch_browser_and_go_to_url(context)


@when(u'I enter using Admin credentials')
def step_impl(context):
    HRMPage.enter_credentials(context)


@when(u'I click the login button')
def step_impl(context):
    HRMPage.click_login(context)


@then(u'I am able to verify the title of the page')
def step_impl(context):
    HRMPage.verify_homepage_title(context)
