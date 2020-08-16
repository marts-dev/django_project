from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from agilelist.models import Statement
from agilelist.serializers import StatementSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class StatementList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Retrieve all statements",
        responses={200: StatementSerializer(many=True)},
    )
    def get(self, request, format=None):
        statements = Statement.objects.all()
        serializer = StatementSerializer(statements, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create new statement",
        request_body=StatementSerializer,
    )
    def post(self, request, format=None):
        serializer = StatementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatementDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        # Can be refactored with django.shortcuts
        try:
            return Statement.objects.get(pk=pk)
        except Statement.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="Retrieve a single statement",
    )
    def get(self, request, pk):
        statement = self.get_object(pk)
        serializer = StatementSerializer(statement)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update statement",
        request_body=StatementSerializer,
    )
    def put(self, request, pk):
        statement = self.get_object(pk)
        serializer = StatementSerializer(statement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="Delete statement",
    )
    def delete(self, request, pk):
        statement = self.get_object(pk)
        statement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ValueList(APIView):
    def get_values(self):
        try:
            return Statement.objects.all().filter(category="value")
        except Statement.DoesNotExist:
            raise Http404
    @swagger_auto_schema(
        operation_description="Retrieve value statements",
        responses={200: StatementSerializer(many=True)},
    )
    def get(self, request):
        statement = self.get_values()
        serializer = StatementSerializer(statement, many=True)
        return Response(serializer.data)

class PrincipleList(APIView):
    def get_principles(self):
        try:
            return Statement.objects.all().filter(category="principle")
        except Statement.DoesNotExist:
            raise Http404
    
    @swagger_auto_schema(
        operation_description="Retrieve principle statements",
        responses={200: StatementSerializer(many=True)},
    )
    def get(self, request):
        statement = self.get_principles()
        serializer = StatementSerializer(statement, many=True)
        return Response(serializer.data)
