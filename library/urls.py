from django.urls import path
from .views import indexPageView, bookPageView, newPageView 
from .views import lastPageView, anotherPageView, listsPageView, searchPageView, searchBooks, addBook

urlpatterns = [
    path('', indexPageView, name='index'),
    path('new/', newPageView, name='new'),
    path('last/', lastPageView, name='last'),
    path('another/', anotherPageView, name='another'),
    path('lists/', listsPageView, name='lists'),
    path('search/', searchPageView, name='search'),
    path('searchbooks/', searchBooks, name="search_books"),
    path('book/add/', addBook, name="add_book"),
    path('<book_id>/', bookPageView, name='book_detail'),
]