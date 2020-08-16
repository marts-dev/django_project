from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_category(category: str):
    if category != "value" and category != "principle":
        raise ValidationError(
            _("%(category)s is not valid, valid values are 'value' or 'principle'"),
            params={"category": category},
        )


# Create your models here.
class Statement(models.Model):
    STATEMENT_TYPE = [
        ("value", "Value"),
        ("principle", "Principle"),
    ]
    title: models.CharField = models.CharField(max_length=255)
    definition: models.TextField = models.TextField(max_length=1000)
    category: models.CharField = models.CharField(
        choices=STATEMENT_TYPE, max_length=9, validators=[validate_category]
    )

    def __str__(self):
        return self.title
