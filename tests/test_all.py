from http import HTTPStatus

import pytest


INDEX_URL = pytest.lazy_fixture('index_url')
CREATE_URL = pytest.lazy_fixture('create_url')
DELETE_URL = pytest.lazy_fixture('delete_url')
GOTO_URL = pytest.lazy_fixture('goto_url')


@pytest.mark.parametrize(
    'url_path, route',
    (
        ('/', INDEX_URL),
        ('/create/', CREATE_URL),
        ('/delete/123/', DELETE_URL),
        ('/go/123/', GOTO_URL),
    )
)
def test_routes(url_path, route):
    assert url_path == route, "Что-то пошло не так"


@pytest.mark.parametrize(
    'route, status',
    (
        (INDEX_URL, HTTPStatus.OK),
        (CREATE_URL, HTTPStatus.FOUND),
        (DELETE_URL, HTTPStatus.FOUND),
        (GOTO_URL, HTTPStatus.FOUND),
    )
)
def test_expected_statuses(route, status, author_client):
    response = author_client.get(route)
    assert response.status_code == status
