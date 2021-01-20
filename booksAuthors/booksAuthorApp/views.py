from django.shortcuts import render, HttpResponse, redirect
from booksAuthorApp.models import Book, Author

# Create your views here.


def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request,"index.html", context)

def add_book(request):
    title_form = request.POST['title']
    desc_form = request.POST['desc']
    Book.objects.create(title=title_form, desc=desc_form)
    return redirect('/')

def show_info_book(request, book_id):
    books_instance = Book.objects.get(id=book_id)
    authors = books_instance.Authors.all()
    context = {
        'book': books_instance,
        'authors': authors,
        'all_authors' : Author.objects.all(),
    }
    return render(request, "show_book.html", context)

def add_author_to_book(request,book_id):
    author_id =request.POST['adding_author']
    this_author = Author.objects.get(id=author_id)
    book_instance = Book.objects.get(id=book_id)
    book_instance.Authors.add(this_author)
    print("where is this")
    return redirect('/show_book/'+str(book_id))

def show_author(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request,"show_author.html", context)

def add_author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    Author.objects.create(
    first_name= first_name,
    last_name= last_name,
    notes=notes)
    return redirect("/authors")

def show_info_authors(request,author_id):
    books = Book.objects.get.all()
    author_instance =Author.objects.get(id=author_id)
    context = {
        'author': author_instance,
        'book' : books,
        'all_books': Books.objects.all()
    }
    return render(request,'author_info.html',context)

def add_book_to_author(request, author_id):
    book_id = request.POST['add_author']
    this_book = Book.objects.get(id=book_id)
    author_instance = Author.objects.get(id=author_id)
    author_instance.book.add(this_book)
    return redirect("/authors_display" + str(author_id))
