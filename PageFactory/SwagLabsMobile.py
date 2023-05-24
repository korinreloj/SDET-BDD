from selenium import webdriver
import time

def launch_swaglabs_application(context):
    app = "C:\\Users\\CorinneJoyceReloj\\Documents\\BPI PROJECT\\TESTING\\SDET TRAINING\\Mobile Automation Testing\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk"
    print(app)

    desired_caps = {
        'deviceName': 'Android Device',
        'deviceId': '5554',
        'platformName': 'Android',
        'appPackage': 'com.swaglabsmobileapp',
        'appActivity': 'com.swaglabsmobileapp.MainActivity',
        'app': app
    }

    print(desired_caps)
    # default appium server: 127.0.0.1
    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    print("Application launched successfully")

def login_standard_user(context):
    usernamefield = context.driver.find_element_by_xpath("//*[@text='Username']")
    usernamefield.click()
    usernamefield.send_keys("standard_user")

    passwordfield = context.driver.find_element_by_xpath("//*[@text='Password']")
    passwordfield.click()
    passwordfield.send_keys("secret_sauce")

    loginbutton = context.driver.find_element_by_xpath("//*[@index='4']")
    loginbutton.click()
    print("Logged in successfully as standard_user")
    time.sleep(2)

def login_locked_out_user(context):
    usernamefield = context.driver.find_element_by_xpath("//*[@text='Username']")
    usernamefield.click()
    usernamefield.send_keys("locked_out_user")

    passwordfield = context.driver.find_element_by_xpath("//*[@text='Password']")
    passwordfield.click()
    passwordfield.send_keys("secret_sauce")

    loginbutton = context.driver.find_element_by_xpath("//*[@index='4']")
    loginbutton.click()
    print("Logged in successfully as locked_out_user")
    time.sleep(2)

def login_problem_user(context):
    usernamefield = context.driver.find_element_by_xpath("//*[@text='Username']")
    usernamefield.click()
    usernamefield.send_keys("problem_user")

    passwordfield = context.driver.find_element_by_xpath("//*[@text='Password']")
    passwordfield.click()
    passwordfield.send_keys("secret_sauce")

    loginbutton = context.driver.find_element_by_xpath("//*[@index='4']")
    loginbutton.click()
    print("Logged in successfully as problem_user")
    time.sleep(2)

def add_to_cart_first_item(context):
    addToCart1 = context.driver.find_element_by_xpath("//*[@text='ADD TO CART']")
    addToCart1.click()
    time.sleep(2)

def go_to_cart(context):
    shoppingCart = context.driver.find_element_by_xpath("//*[@index='3']")
    shoppingCart.click()
    time.sleep(2)

def hamburger_logout(context):
    hamburger_button = context.driver.find_element_by_xpath("//*[@content-desc='test-Menu']")
    hamburger_button.click()
    time.sleep(2)

    logout = context.driver.find_element_by_xpath("//*[@text='LOGOUT']")
    logout.click()
    time.sleep(2)

def verify_swaglabs(context):
    login_page = context.driver.find_element_by_xpath("//*[@content-desc='test-Login']")
    assert login_page.is_displayed()
    print("Back to Login Page:::Test Successful")

    context.driver.close()