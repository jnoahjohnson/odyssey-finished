from django.urls import path
from .views import indexPageView, bookPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('/<book_id>', bookPageView, name='book_detail')
]