# coding: utf-8
import unittest
from time import sleep
import time
from case.base_case import BaseCase
from public.screenshot import insert_img
from pages.my_class_page import MyClassPage


class MyClassCase(BaseCase):

    # @unittest.skip
    def test_load_featured_class_success(self):
        """跳转到精选课程"""

        my_class_page = MyClassPage(self.dr)
        my_class_page.switch_featured_class()
        insert_img(self.dr, "跳转到精选课程成功.jpg")

    def test_load_featured_note_success(self):
        """跳转到精选笔记"""

        my_class_page = MyClassPage(self.dr)
        my_class_page.switch_featured_note()
        insert_img(self.dr, "跳转到精选笔记成功.jpg")


if __name__ == '__main__':
    unittest.main()
    # 构造测试集
    # suite = unittest.TestSuite()
    # # suite.addTest(MyClassCase("test_load_featured_class_success"))
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
