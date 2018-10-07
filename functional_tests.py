# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        # 隐式等待
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_start_a_list_and_retrieve_it_later(self):
        # 打开应用首页
        self.browser.get('http://localhost:8000/')

        # 应用网页标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请用户输入待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 用户在文本框中输入“Buy peacock feathers”
        inputbox.send_keys('Buy peacock feathers')

        # 用户按回车键后，页面更新了
        # 待办事项列表中显示了“1：Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1:Buy peacock feathers')

        # 页面中显示一个文本框，可以输入其他的待办事项
        # 用户输入了“Use peacock feathers to make a fly”
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        import time
        time.sleep(5)
        # 页面再次更新，清单中显示这两个待办事项
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        self.check_for_row_in_list_table('2:Use peacock feathers to make a fly')

        # 验证网站是否会记住用户的清单
        # 用户看到网站为他生成了一个唯一的URL
        # 而且页面中有写文字解析这个功能

        # 用户访问URL，发现用户的待办列表还在


if __name__ == '__main__':
    unittest.main()