from behave import given
from PageFactory import TestOne

@given(u'I am able to open the chrome browser')
def step_impl(context):
    TestOne.launch_browser(context)