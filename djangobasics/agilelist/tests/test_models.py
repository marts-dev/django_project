from agilelist.models import Statement
import factories
import pytest


@pytest.mark.django_db
class TestModels:
    def test_statement_created(self):
        statement = factories.StatementFactory()
        assert statement.title == "test title 0"
        assert statement.definition == "test title 0 test definition"
        assert statement.category == "test category"
