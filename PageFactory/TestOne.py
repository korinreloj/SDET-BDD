import time
from selenium import webdriver

def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path="C:/Users/CorinneJoyceReloj/PycharmProjects/SDETBDD/drivers/chromedriver.exe")
    time.sleep(2)
    context.driver.get("https://www.google.com/")
    time.sleep(2)