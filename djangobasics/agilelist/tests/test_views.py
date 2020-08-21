import pytest
import json
import factories
from django.urls import reverse
from rest_framework import status
from agilelist.models import Statement
from agilelist.serializers import StatementSerializer


@pytest.mark.getmethods
@pytest.mark.django_db
class TestGetStatements:
    def setup_method(cls):
        factories.StatementFactory()
        factories.StatementFactory()

    def test_get_all_statements(self, client):
        response = client.get(reverse("agilelist:statements-list"))
        statements = Statement.objects.all()
        serializer = StatementSerializer(statements, many=True)
        assert response.data == serializer.data
        assert response.status_code == status.HTTP_200_OK

    def test_get_all_value_statements(self, client):
        factories.StatementFactory(category="value")
        response = client.get(reverse("agilelist:values-list"))
        statements = Statement.objects.all().filter(category="value")
        serializer = StatementSerializer(statements, many=True)
        print(serializer.data)
        assert response.data == serializer.data
        assert response.status_code == status.HTTP_200_OK

    def test_get_all_principle_statements(self, client):
        factories.StatementFactory(category="principle")
        response = client.get(reverse("agilelist:principles-list"))
        statements = Statement.objects.all().filter(category="principle")
        serializer = StatementSerializer(statements, many=True)
        assert response.data == serializer.data
        assert response.status_code == status.HTTP_200_OK

    def test_get_valid_statement(self, client):
        response = client.get(reverse("agilelist:statements-detail", kwargs={"pk": 2}))
        statement = Statement.objects.last()
        serializer = StatementSerializer(statement)
        assert response.data == serializer.data
        assert response.status_code == status.HTTP_200_OK

    def test_get_invalid_statement(self, client):
        invalid_pk = 0
        response = client.get(
            reverse("agilelist:statements-detail", kwargs={"pk": invalid_pk})
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.writemethods
@pytest.mark.django_db
class TestPostPutDeleteStatements:
    def setup_method(cls):
        factories.StatementFactory()
        factories.StatementFactory()

    def test_create_valid_statement(self, client, django_user_model):
        valid_payload = {
            "title": "Test title",
            "definition": "Test def",
            "category": "value",
        }
        username = "user1"
        password = "bar"
        django_user_model.objects.create_user(username=username, password=password)
        client.login(username=username, password=password)
        response = client.post(
            reverse("agilelist:statements-list"),
            data=json.dumps(valid_payload),
            content_type="application/json",
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_invalid_statement(self, client, django_user_model):
        valid_payload = {
            "title": "Test title",
            "definition": "Test def",
            "category": "",
        }
        username = "user1"
        password = "bar"
        django_user_model.objects.create_user(username=username, password=password)
        client.login(username=username, password=password)
        response = client.post(
            reverse("agilelist:statements-list"),
            data=json.dumps(valid_payload),
            content_type="application/json",
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_update_valid_statement(self, client, django_user_model):
        valid_payload = {
            "title": "Test title",
            "definition": "Test def",
            "category": "value",
        }
        statement = Statement.objects.last()
        username = "user1"
        password = "bar"
        django_user_model.objects.create_user(username=username, password=password)
        client.login(username=username, password=password)
        response = client.put(
            reverse("agilelist:statements-detail", kwargs={"pk": statement.pk}),
            data=json.dumps(valid_payload),
            content_type="application/json",
        )
        assert response.status_code == status.HTTP_200_OK

    def test_update_invalid_statement(self, client, django_user_model):
        invalid_payload = {
            "title": "",
            "definition": "Test def",
            "category": "value",
        }
        statement = Statement.objects.last()
        username = "user1"
        password = "bar"
        django_user_model.objects.create_user(username=username, password=password)
        client.login(username=username, password=password)
        response = client.put(
            reverse("agilelist:statements-detail", kwargs={"pk": statement.pk}),
            data=json.dumps(invalid_payload),
            content_type="application/json",
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_update_not_existing_statement(self, client, django_user_model):
        invalid_payload = {
            "title": "",
            "definition": "Test def",
            "category": "value",
        }
        invalid_pk = 0
        username = "user1"
        password = "bar"
        django_user_model.objects.create_user(username=username, password=password)
        client.login(username=username, password=password)
        response = client.put(
            reverse("agilelist:statements-detail", kwargs={"pk": invalid_pk}),
            data=json.dumps(invalid_payload),
            content_type="application/json",
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_not_existing_statement(self, client, django_user_model):
        username = "user1"
        password = "bar"
        invalid_pk = 0
        django_user_model.objects.create_user(username=username, password=password)
        client.login(username=username, password=password)
        response = client.delete(
            reverse("agilelist:statements-detail", kwargs={"pk": invalid_pk}),
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_valid_statement(self, client, django_user_model):
        username = "user1"
        password = "bar"
        statement = Statement.objects.last()
        django_user_model.objects.create_user(username=username, password=password)
        client.login(username=username, password=password)
        response = client.delete(
            reverse("agilelist:statements-detail", kwargs={"pk": statement.pk}),
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT
