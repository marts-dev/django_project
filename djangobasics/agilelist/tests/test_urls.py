from django.urls import reverse, resolve


class TestUrls:
    def test_statement_list(self):
        path = reverse("agilelist:list")
        assert resolve(path).view_name == "agilelist:list"
    def test_statement_detail(self):
        path = reverse("agilelist:detail", kwargs={"pk":1})
        assert resolve(path).view_name == "agilelist:detail"
    def test_statement_values(self):
        path = reverse("agilelist:values")
        assert resolve(path).view_name == "agilelist:values"
    def test_statement_principles(self):
        path = reverse("agilelist:principles")
        assert resolve(path).view_name == "agilelist:principles"
