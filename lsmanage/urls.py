from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home-page'),
    path('adminlogin', views.admin_login, name='admin-login'),
    path('admindashboard', views.admin_dashboard, name='admin-dashboard'),
    path('addlibrarian', views.add_librarian, name='add-librarian'),
    path('viewlibrarian', views.view_librarian, name='view-librarian'),
    path('deletelibrarian/<int:id>', views.delete_librarian, name='delete-librarian'),

    # Librarian views

    path('librarianlogin', views.librarian_login, name='librarian-login'),
    path('librariandashboard', views.librarian_dashboard, name='librarian-dashboard'),
    path('addbook', views.add_book, name='add-book'),
    path('viewbooks', views.view_books, name='view-books'),
    path('issuebook', views.issue_book, name='issue-book'),
    path('logout', views.logout, name='logout'),
]