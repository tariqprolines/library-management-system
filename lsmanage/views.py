from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import login, authenticate,logout as auth_logout
from .forms import UserForm, BookForm, IssueBookForm, ReturnBookForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Book, IssueBook

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

@login_required(login_url='/adminlogin')
def admin_dashboard(request):
    return render(request,'lsmanage/admin_dashboard.html')

@login_required(login_url='/adminlogin')
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

@login_required(login_url='/adminlogin')
def view_librarian(request):
    librarians = User.objects.filter(is_staff=False)
    return render(request,'lsmanage/view_librarian.html',{'librarians':librarians})

@login_required(login_url='/adminlogin')
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

@login_required(login_url='/librarianlogin')
def librarian_dashboard(request):
    return render(request,'lsmanage/librarian_dashboard.html')       

@login_required(login_url='/librarianlogin')
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

@login_required(login_url='/librarianlogin')    
def view_books(request):
    books=Book.objects.all()
    return render(request, 'lsmanage/view_books.html',{'books':books})  
    
def issue_book(request):
    if request.method== 'POST':
        issuebook_form= IssueBookForm(request.POST)
        if issuebook_form.is_valid:
            book_id=request.POST.get('book')
            stud_id=request.POST.get('student_id')
            studentname=request.POST.get('student_name')
            issued_book_status= IssueBook.objects.filter(student_id=stud_id,book_id=book_id)
            if issued_book_status is not None:
                messages.warning(request,f'{studentname} already has this book.')
            else:    
                books=Book.objects.filter(id=book_id).values('quantity','issued')[0]
                if book['quantity'] > 0:
                    quantity=books['quantity']-1
                    issued = books['issued']+1
                    update_book= Book.objects.filter(id=book_id).update(quantity=quantity,issued=issued)
                    issuebook_form.save()
                    messages.success(request,f'Book has been issued to "{studentname}"')
                else:
                    messages.warning(request, 'This book has not enough quantiy for issue.')    
        else:
            messages.error(request,'Something Wrong in form submission.')    
    else:
        issuebook_form=IssueBookForm()
    return render(request,'lsmanage/issue_book.html', {'issuebook_form':issuebook_form})      

def view_issued_books(request):
    issued_books= IssueBook.objects.all().select_related('book')
    return render(request, 'lsmanage/view_issued_books.html',{'issued_books':issued_books})    

def return_book(request):
    if request.method == 'POST':
        return_form=ReturnBookForm(request.POST)
        if return_form.is_valid:
            messages.success(request,'Book has returned successfully.')
    else:
        return_form=ReturnBookForm()        
    return render(request, 'lsmanage/return_book.html',{'return_form':return_form})           

def logout(request):
    auth_logout(request)
    return redirect('home-page')