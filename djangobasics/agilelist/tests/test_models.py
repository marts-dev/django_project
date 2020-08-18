import factories
import pytest
from agilelist.models import Statement


@pytest.mark.statementmodels
@pytest.mark.django_db
class TestModels:
    def setup_method(self):
        factories.StatementFactory()
        factories.StatementFactory()

    def test_statement_created(self):
        statement = factories.StatementFactory()
        query = Statement.objects.last()
        statement_count = Statement.objects.count()
        assert statement.title == query.title
        assert statement_count == 3

    def test_statement_updated(self):
        statement = factories.StatementFactory()
        Statement.objects.filter(pk=statement.pk).update(title="updated")
        query = Statement.objects.last()
        statement_count = Statement.objects.count()
        assert query.title == "updated"
        assert statement_count == 3

    def test_statement_deleted(self):
        statement = factories.StatementFactory()
        Statement.objects.filter(pk=statement.pk).delete()
        query = Statement.objects.last()
        statement_count = Statement.objects.count()
        assert query.id == 2
        assert statement_count == 2
