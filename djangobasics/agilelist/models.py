from django.db import models

# Create your models here.
class Statement(models.Model):
    STATEMENT_TYPE = [
        ("value", "Value"),
        ("principle", "Principle"),
    ]
    title: models.CharField = models.CharField(max_length=255)
    definition: models.TextField = models.TextField(max_length=1000)
    category: models.CharField = models.CharField(choices=STATEMENT_TYPE, max_length=9)

    def __str__(self):
        return self.title