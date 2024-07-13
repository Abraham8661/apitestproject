from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from Blog.models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def api_home_view(request, **args):
    data = {}
    instance = Book.objects.all().order_by('publishDate').first()

    if instance:
        data = BookSerializer(instance).data
    return Response(data)

class allBooks(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

