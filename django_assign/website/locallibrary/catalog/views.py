from django.shortcuts import render

# Create your views here.

from catalog.models import Book, Author, Genre

def index(request):



    num_books = Book.objects.all().count()
   


    
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
    }

    
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
class BookDetailView(generic.DetailView):
    model = Book

from django.views import generic

class BookListView(generic.ListView):
    model = model
