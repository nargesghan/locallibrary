from django.contrib import admin
from .models import Book,Author,BookInstance,Genre
# Register your models here.


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter=('status','due_back')

    fieldsets= (
        ('Information', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    inlines = [BooksInstanceInline]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]