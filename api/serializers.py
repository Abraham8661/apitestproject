from rest_framework import serializers
from Blog.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publishingCountry', 'publishDate']