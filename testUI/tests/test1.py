from testUI.POM.main_page import MainPage
from selenium import webdriver
from data.data_UI import *

driver = webdriver.Chrome()

main_page = MainPage()
main_page.enter_login(driver, LOGIN)
