from django.urls import path
from .views import indexPageView, bookPageView, newPageView, lastPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('new/', newPageView, name='new'),
    path('last/', lastPageView, name='last'),
    path('<book_id>/', bookPageView, name='book_detail')
]