from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, IssueBook,  MyUser
from .forms import MyUserForm, UpdateUserForm

admin.site.register(Book)
admin.site.register(IssueBook)

class MyUserAdmin(UserAdmin):
    add_form = MyUserForm
    form = UpdateUserForm
    model = MyUser
    list_display = ['username','first_name','last_name','email','phone','address','city',]

admin.site.register(MyUser, MyUserAdmin)
