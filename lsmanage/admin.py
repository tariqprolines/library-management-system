from django.contrib import admin
from .models import Book, IssueBook, Profile

admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(IssueBook)
