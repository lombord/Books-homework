from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (TemplateView, DeleteView,
                                  CreateView, UpdateView,
                                  ListView, DetailView)

from .models import *
from .forms import *


class HomeView(TemplateView):
    template_name = "base/home.html"


# Book views
class AddBookView(CreateView):
    form_class = BookForm
    template_name = "base/form.html"
    extra_context = {'title': 'Add a book', 'submit': 'add'}


class EditBookView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "base/form.html"
    extra_context = {'title': 'Edit a book', 'submit': 'Edit'}


class DeleteBookView(DeleteView):
    model = Book
    success_url = reverse_lazy("books")
    template_name = "base/form.html"
    extra_context = {'title': 'Delete a book', 'submit': 'Delete'}


class BooksView(ListView):
    model = Book
    template_name = "base/books.html"
    context_object_name = 'books'


class BookView(DetailView):
    model = Book
    template_name = "base/book.html"
    context_object_name = "book"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        response = super().get(request, *args, **kwargs)
        self.object.increase_views()
        return response


# Author views
class AddAuthorView(CreateView):
    model = Author
    fields = "__all__"
    extra_context = {'title': 'Add an Author', 'submit': 'Add'}
    template_name = "base/form.html"
    success_url = reverse_lazy("add_book")


# Author views
class AddGenreView(CreateView):
    model = Genre
    fields = "__all__"
    template_name = "base/form.html"
    extra_context = {'title': 'Create a Genre', 'submit': 'Create'}
    success_url = reverse_lazy("add_book")
