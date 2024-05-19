from django.urls import path,include
from .views import BookSearchView,BookViewSet,UserInteractionViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'user-interactions', UserInteractionViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('search/', BookSearchView.as_view(), name='book_search'),
]