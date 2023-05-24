from behave import given
from behave import when
from behave import then
from PageFactory import SwagLabsMobile

@given(u'I am able to open the application')
def step_impl(context):
    SwagLabsMobile.launch_swaglabs_application(context)

@when(u'I enter using standard_user credentials')
def step_impl(context):
    SwagLabsMobile.login_standard_user(context)

@when(u'I enter using locked_out_user credentials')
def step_impl(context):
    SwagLabsMobile.login_locked_out_user(context)

@when(u'I enter using problem_user credentials')
def step_impl(context):
    SwagLabsMobile.login_problem_user(context)

@when(u'I add to cart the first item')
def step_impl(context):
    SwagLabsMobile.add_to_cart_first_item(context)

@when(u'go to cart')
def step_impl(context):
    SwagLabsMobile.go_to_cart(context)

@when(u'click hamburger and choose logout')
def step_impl(context):
    SwagLabsMobile.hamburger_logout(context)

@then(u'I am able to test SwagLabs Mobile')
def step_impl(context):
    SwagLabsMobile.verify_swaglabs(context)