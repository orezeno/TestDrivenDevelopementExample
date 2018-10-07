from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
from django.shortcuts import render_to_response


# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
        """
            通过render_to_response返回的内容会比实际通过home_page函数返回缺少
            csrf_token内容
            而且 render_to_string在2.1.2中不存在
        """
        # expected_page = render_to_response(
        #     'home.html',
        #     {'new_item_text': 'A new list item'}
        # )
        # self.assertEqual(response.content.decode(), expected_page.content.decode())