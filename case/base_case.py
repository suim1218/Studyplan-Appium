import unittest
from appium import webdriver
from pages.login_page import LoginPage
from time import sleep


class BaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['automationName'] = 'Appium'
        desired_caps['deviceName'] = 'msm8953_64'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['noReset'] = True
        desired_caps["appPackage"] = "com.begoit.studyplan"
        desired_caps["appActivity"] = ".ui.act.SplashActivity"
        cls.dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(5)
        po = LoginPage(cls.dr)
        po.login_success('13312340001', '')

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
