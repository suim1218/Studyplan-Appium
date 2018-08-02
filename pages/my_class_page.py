from pages.base_page import BasePage
from time import sleep


class MyClassPage(BasePage):
    @property
    def featured_class(self):
        return self.by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
            'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.'
            'RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.'
            'widget.HorizontalScrol'
            'lView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView')

    @property
    def featured_note(self):
        return self.by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
            '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android'
            '.view.ViewGroup/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.'
            'LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView')

    # 跳转到精选课程
    def switch_featured_class(self):
        self.featured_class.click()
        sleep(1.5)

    # 跳转到精选笔记
    def switch_featured_note(self):
        self.featured_note.click()
        sleep(1.5)
