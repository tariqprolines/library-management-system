from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import login, authenticate,logout as auth_logout
from .forms import UserForm, BookForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Book

def index(request):
    return render(request,'lsmanage/index.html')
def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser==True:
        return redirect('admin-dashboard')
    else:    
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('admin-dashboard')
            else:
                messages.error(request, 'Username or Password is not correct!')
        return render(request,'lsmanage/adminlogin.html')

def admin_dashboard(request):
    return render(request,'lsmanage/admin_dashboard.html')

def add_librarian(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username=request.POST.get('username')
            messages.success(request, f'{username} added successfully as a Librarian!')
            return redirect('add-librarian')
    else:
        user_form = UserForm()
    return render(request, 'lsmanage/add_librarian.html', {
        'user_form': user_form
    })

def view_librarian(request):
    librarians = User.objects.filter(is_staff=False)
    return render(request,'lsmanage/view_librarian.html',{'librarians':librarians})

def delete_librarian(request,id):
    username=User.objects.filter(id=id)
    dellibrarian= User.objects.filter(id=id).delete()   
    if dellibrarian:
        messages.success(request, f'{username} has been deleted successfully!')
        return redirect('view-librarian')

# Librarian Views

def librarian_login(request):
    if request.user.is_authenticated and request.user.is_superuser==False:
        return redirect('librarian-dashboard')
    else:    
        if request.method=='POST':
                username=request.POST.get('username')
                password=request.POST.get('password')
                user=authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('librarian-dashboard')
                else:
                    messages.error(request, 'Username or Password is not correct!')
        return render(request, 'lsmanage/librarian_login.html')  

def librarian_dashboard(request):
    return render(request,'lsmanage/librarian_dashboard.html')       

def add_book(request):
    if request.method=='POST':
        book_form=BookForm(request.POST)
        if book_form.is_valid:
            form=book_form.save(commit=False)
            form.user=request.user
            form.save()
            book=request.POST.get('name')
            messages.success(request,f'"{book}" book has been added successfully.')
        else:
            messages.error(request,'Something Wrong.')  
    else:
        book_form=BookForm()          
    return render(request, 'lsmanage/add_book.html',{'book_form':book_form}) 
def view_books(request):
    books=Book.objects.all()
    return render(request, 'lsmanage/view_books.html',{'books':books})  
def issue_book(request):
    return HttpResponse('Issue Book')             

def logout(request):
    auth_logout(request)
    return redirect('home-page')