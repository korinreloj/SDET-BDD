import time
from selenium import webdriver

def launch_browser_and_go_to_url(context):
    url = "http://hrm.syntaxtechs.net/humanresources/symfony/web/index.php/auth/login"
    context.driver = webdriver.Chrome(executable_path="C:/Users/CorinneJoyceReloj/PycharmProjects/SDETBDD/drivers/chromedriver.exe")
    time.sleep(2)
    context.driver.get(url)
    time.sleep(2)

def enter_credentials(context):
    username = "Admin"
    password = "Hum@nhrm123"
    username_input = context.driver.find_element_by_xpath("//*[@id='txtUsername']")
    username_input.send_keys(username)
    time.sleep(2)

    password_input = context.driver.find_element_by_xpath("//*[@id='txtPassword']")
    password_input.send_keys(password)
    time.sleep(2)

def click_login(context):
    login_button = context.driver.find_element_by_xpath("//*[@id='btnLogin']")
    login_button.click()

def verify_homepage_title(context):
    homepage_title ="Human Management System"
    actual_title = context.driver.title
    assert actual_title == homepage_title
    print(actual_title)
    time.sleep(2)

