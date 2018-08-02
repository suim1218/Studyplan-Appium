from pages.base_page import BasePage
from time import sleep


class LoginPage(BasePage):
    @property
    def mobile_textfield(self):
        return self.by_id('com.begoit.studyplan:id/mobile_layout')

    @property
    def password_textfield(self):
        return self.by_id('com.begoit.studyplan:id/password')

    @property
    def login_btn(self):
        return self.by_id('com.begoit.studyplan:id/login_button')

    def login_success(self, username, password):
        self.mobile_textfield.clear()
        self.mobile_textfield.send_keys(username)
        self.password_textfield.clear()
        self.password_textfield.send_keys(password)
        self.hide_keyboard()
        self.login_btn.click()
        sleep(2)
