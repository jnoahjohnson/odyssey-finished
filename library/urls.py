from django.urls import path
from .views import indexPageView, bookPageView, newPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('new/', newPageView, name='new'),
    path('<book_id>/', bookPageView, name='book_detail')
]