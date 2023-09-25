from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from .models import User, Url


class TestUrls(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='Ivan')
        cls.url = Url.objects.create(
            author=cls.user,
            full_url='https://ya.ru/',
            shorted_url='abc'
        )
        cls.INDEX_URL = reverse('index')
        cls.CREATE_URL = reverse('create_url')
        cls.DELETE_URL = reverse('delete_url', args=(cls.url.shorted_url,))
        cls.GOTO_URL = reverse('goto', args=(cls.url.shorted_url,))
    cls.urls = {
            cls.INDEX_URL: ('/', HTTPStatus.OK),
            cls.CREATE_URL: ('/create/', HTTPStatus.FOUND),
            cls.DELETE_URL: (f'/delete/{cls.url.shorted_url}/', HTTPStatus.FOUND),
            cls.GOTO_URL: (f'/go/{cls.url.shorted_url}/', HTTPStatus.FOUND),
        }

    def setUp(self):
        pass

# / - index
# /create/ - создать ссылку
# /delete/<slug> - удалить ссылку
# /go/<slug> - перейти по ссылке

    def test_routes(self):
        for test_reverse, (expected_url, _) in self.urls.items():  # (cls.INDEX_URL, ('/', HTTPStatus.OK))
            with self.subTest(
                test_reverse=test_reverse,
                expected_url=expected_url
            ):
                self.assertEqual(test_reverse, expected_url)


    def test_pages_return_expected_statuses(self):
        for test_reverse, (_, expected_status) in self.urls.items():
            with self.subTest(test_reverse, expected_status=expected_status):
                response = self.client.get(test_reverse)
                self.assertEqual(response.status_code, expected_status)
