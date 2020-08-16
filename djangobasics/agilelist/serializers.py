from rest_framework import serializers
from agilelist.models import Statement


class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = ["id", "title", "definition", "category"]
