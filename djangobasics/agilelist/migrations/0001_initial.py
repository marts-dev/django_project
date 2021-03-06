# Generated by Django 3.1 on 2020-08-16 19:20

import agilelist.models
from typing import List
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: List[str] = []

    operations = [
        migrations.CreateModel(
            name="Statement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("definition", models.TextField(max_length=1000)),
                (
                    "category",
                    models.CharField(
                        choices=[("value", "Value"), ("principle", "Principle")],
                        max_length=9,
                        validators=[agilelist.models.validate_category],
                    ),
                ),
            ],
        ),
    ]
