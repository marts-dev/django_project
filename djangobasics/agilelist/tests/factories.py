import factory


class StatementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "agilelist.Statement"
        django_get_or_create = ("title", "definition", "category")

    title = factory.Sequence(lambda n: "test title %s" % n)
    definition = factory.LazyAttribute(lambda o: "%s test definition" % o.title)
    category = "test category"
