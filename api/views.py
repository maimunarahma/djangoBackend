from rest_framework import mixins,viewsets,filters
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    http_method_names = ['get', 'post', 'put', 'delete', 'patch']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'price']   # exact filters
    search_fields = ['title', 'author']      # search by keyword
    ordering_fields = ['price', 'published_date']
