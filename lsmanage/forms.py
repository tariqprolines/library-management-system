from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, IssueBook, Profile

class UserForm(UserCreationForm):
	first_name=forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name=forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		model=User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
	phone= forms.CharField(max_length=30, required=False)
	address= forms.CharField(max_length=100, required=False)
	city= forms.CharField(max_length=30, required=False)

	class Meta:
		model=Profile
		fields=('phone','address','city')
    	
    
class BookForm(forms.ModelForm):
	call_no=forms.CharField(max_length=20, help_text='Required')
	name=forms.CharField(max_length=30, help_text='Required')
	author=forms.CharField(max_length=30, help_text='Required')
	publisher=forms.CharField(max_length=50, help_text='Required')
	quantity=forms.IntegerField()

	class Meta:
		model= Book
		fields=('call_no', 'name', 'author', 'publisher', 'quantity')

class IssueBookForm(forms.ModelForm):

	student_id=forms.IntegerField()
	student_name=forms.CharField(max_length=30,)
	student_contact=forms.CharField(max_length=20,)

	class Meta:
		model= IssueBook
		fields= ('book','student_id','student_name','student_contact')

class ReturnBookForm(forms.ModelForm):

	student_id=forms.IntegerField()

	class Meta:
		model= IssueBook
		fields= ('book','student_id')		
	






