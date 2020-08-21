import pytest
from django.urls import reverse, resolve


@pytest.mark.agilelinks
class TestUrls:
    def test_statement_list(self):
        path = reverse("agilelist:statements-list")
        assert resolve(path).view_name == "agilelist:statements-list"

    def test_statement_detail(self):
        path = reverse("agilelist:statements-detail", kwargs={"pk": 1})
        assert resolve(path).view_name == "agilelist:statements-detail"

    def test_statement_values(self):
        path = reverse("agilelist:values-list")
        assert resolve(path).view_name == "agilelist:values-list"

    def test_statement_principles(self):
        path = reverse("agilelist:principles-list")
        assert resolve(path).view_name == "agilelist:principles-list"
