from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm
from .models import Book

def index(request):
    return render(request, 'books/index.html')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'status']
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'status']
    success_url = reverse_lazy('book_list')

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
