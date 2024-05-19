from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
from .utils import fetch_book_data

class BookSearchView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        author = request.GET.get('author', '')
        category = request.GET.get('category', '')
        if not query:
            return JsonResponse({'error': 'Query parameter is required'}, status=400)
        data = fetch_book_data(query, author, category)

        # data1=data["items"][0]["volumeInfo"]
        # for i in range(data["items"])
        if 'items' in data:
            # Get only the first 5 items from the 'items' list
            items = data['items'][:5]
            # Create a new list to store the simplified book data
            simplified_items = []
            for item in items:
                # Extract only the 'title', 'authors', and 'description' from 'volumeInfo'
                volume_info = item.get('volumeInfo', {})
                simplified_item = {
                    'title': volume_info.get('title'),
                    'authors': volume_info.get('authors'),
                    'description': volume_info.get('description'),
                    'ratings': volume_info.get('ratingsCount'),
                    'images': volume_info.get('imageLinks'),


                }
                simplified_items.append(simplified_item)  # Add the simplified item to the list
        # data2=data["items"][0]["volumeInfo"]
        return render(request,'book_dashboard.html',{'book_detail':simplified_items})
        # return JsonResponse(data)
# views.py

from rest_framework import viewsets
from rest_framework import filters

from .models import Book, UserInteraction
from .serializers import BookSerializer, UserInteractionSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['genre', 'rating', 'publication_date']
    search_fields = ['title', 'author', 'genre']  # Define fields for search

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset



class UserInteractionViewSet(viewsets.ModelViewSet):
    queryset = UserInteraction.objects.all()
    serializer_class = UserInteractionSerializer
