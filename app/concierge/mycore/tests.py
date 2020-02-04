import json
from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse

from concierge.settings import FIXTURES


class ViewTests(TestCase):
    client = Client()
    fixtures = FIXTURES

    def test_views(self):
        views = ['index', 'health_check', 'tenant', 'room', 'journal']
        for view in views:
            with self.subTest(view=view):
                response = self.client.get(reverse(view))
                assert response.status_code == HTTPStatus.OK

    def test_detail_view(self):
        response = self.client.get(reverse('tenant-detail', kwargs={'pk': 1}))
        assert response.status_code == HTTPStatus.OK

    def test_api_serializer_view(self):
        response = self.client.get(reverse('api', args=['tenant', 1]), {'format': 'json'})
        assert response.status_code == HTTPStatus.OK


class ApiTest(TestCase):

    fixtures = FIXTURES

    def test_api_serializer(self):
        response = self.client.get(reverse('api', args=['tenant', 1]), {'format': 'json'})
        assert json.loads(response.content.decode('utf-8')) == \
            [{"model": "mycore.tenant", "pk": 1, "fields":
                {"first_name": "John", "last_name": "Lennon", "date_of_birth": "1940-10-09",
                 "phone": "+380999248316", "photo": "", "notes": "musician"}}]
