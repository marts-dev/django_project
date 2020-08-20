from django.http import Http404
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from agilelist.models import Statement
from agilelist.serializers import StatementSerializer
from drf_yasg.utils import swagger_auto_schema


class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Retrieve value statements",
        responses={200: StatementSerializer(many=True)},
    ),
)
class ValueList(viewsets.ReadOnlyModelViewSet):
    serializer_class = StatementSerializer

    def get_queryset(self):
        try:
            return Statement.objects.all().filter(category="value")
        except Statement.DoesNotExist:
            raise Http404


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="Retrieve principle statements",
        responses={200: StatementSerializer(many=True)},
    ),
)
class PrincipleList(viewsets.ReadOnlyModelViewSet):
    serializer_class = StatementSerializer

    def get_queryset(self):
        try:
            return Statement.objects.all().filter(category="principle")
        except Statement.DoesNotExist:
            raise Http404
