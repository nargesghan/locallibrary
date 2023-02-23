from django.shortcuts import render
from .models import Book,Author,BookInstance,Genre
# Create your views here.

from django.views import generic

class index(generic.TemplateView):
    template_name='catalog/index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['num_books']=Book.objects.all().count()
        context['num_instances']=BookInstance.objects.all().count()
        context['num_instances_available']=BookInstance.objects.filter(status__exact='a').count()
        context['num_authors']=Author.objects.count()
        return context

class BookListView(generic.ListView):
    model = Book
    template_name='catalog/book_list.html'
    # context_object_name = 'my_book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
class BookDetailView(generic.ListView):
    model=Book
    template_name='catalog/book_detail.html'
# def index(request):

#     num_books=Book.objects.all().count()
#     num_instances=BookInstance.objects.all().count()
#     num_instances_available=BookInstance.objects.filter(status__exact='a').count()
#     num_authors=Author.objects.count()

#     #Render the HTML template index.html with the data in the context variable
#     return render(
#         request,
#         'catalog/index.html',
#         context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors}
#     )

class AuthorListView(generic.ListView):
    model=Author
    template_name='catalog/author_list.html'