from django.urls import reverse
import pytest

from shortener.models import Url


@pytest.fixture
def url(author):
    return Url.objects.create(
        author=author,
        full_url='https://ya.ru/',
        shorted_url='123'
    )


@pytest.fixture 
def author(django_user_model):  # class Author... author = Author(...)
    return django_user_model.objects.create_user(username='Ivan')


@pytest.fixture
def author_client(author, client):
    client.force_login(author)
    return client


@pytest.fixture
def index_url():
    return reverse('index')


@pytest.fixture
def create_url():
    return reverse('create_url')


@pytest.fixture
def delete_url(url):
    return reverse('delete_url', args=(url.shorted_url,))


@pytest.fixture
def goto_url(url):
    return reverse('goto', args=(url.shorted_url,))
