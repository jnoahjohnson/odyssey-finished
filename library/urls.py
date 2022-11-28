from django.urls import path
from .views import indexPageView, bookPageView, newPageView, lastPageView, anotherPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('new/', newPageView, name='new'),
    path('last/', lastPageView, name='last'),
    path('another/', anotherPageView, name='another'),
    path('<book_id>/', bookPageView, name='book_detail')
]