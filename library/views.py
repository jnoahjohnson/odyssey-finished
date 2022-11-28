from django.shortcuts import render
from .models import Book, List

book_list = {
    '1': {
        'id': '1',
        'title': 'The Way of Kings',
        'author': 'Brandon Sanderson',
        'price': 10.99,
        'image': 'https://m.media-amazon.com/images/I/51ZX3mqLFzL.jpg'
    },
    '2': {
        'id': '2',
        'title': 'The Name of the Wind',
        'author': 'Patrick Rothfuss',
        'price': 8.99,
        'image': 'https://m.media-amazon.com/images/I/51JThzjy3gL._AC_SY780_.jpg'
    },
    '3': {
        'id': '3',
        'title': 'Mistborn',
        'author': 'Brandon Sanderson',
        'price': 9.99,
        'image': 'https://m.media-amazon.com/images/I/51sKzl+R6OL._AC_SY780_.jpg'
    }
}

# Create your views here.
def indexPageView(request):
    db_books = Book.objects.all()

    for book in db_books:
        print(book.author.name)

    context = {
        'books': db_books
    }
    return render(request, 'library/index.html', context)


def bookPageView(request, book_id):
    # find book in book list given a title

    context = {
        'book': Book.objects.get(id=book_id)
    }

    return render(request, 'library/book.html', context)

def newPageView(request):
    return render(request, "library/new.html")

def lastPageView(request):
    return render(request, 'library/last.html')

def anotherPageView(request):
    return render(request, "library/another.html")


def listsPageView(request):
    lists = List.objects.all()

    context = {
        'lists': lists
    }

    return render(request, 'library/lists.html', context)