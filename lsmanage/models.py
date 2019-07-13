from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class MyUser(AbstractUser):
    phone=models.CharField(max_length=20,null=True,)
    address=models.TextField(null=True, blank=True)
    city=models.CharField(max_length=30,null=True,)

    def __str__(self):
        return self.username

class Book(models.Model):
	id= models.AutoField(primary_key=True)
	call_no= models.CharField(max_length=20, null=True, blank= True, unique=True)
	name=models.CharField(max_length=30, null=True, blank= True)
	author=models.CharField(max_length=30, null=True, blank=True)
	publisher=models.CharField(max_length=50, null=True, blank=True)
	quantity=models.IntegerField(default=0)
	issued=models.IntegerField(default=0)
	created_date=models.DateField(auto_now_add=True)
	user=models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name

class IssueBook(models.Model):
	id= models.AutoField(primary_key=True)
	student_id=models.IntegerField(null=True, blank=True)
	student_name=models.CharField(max_length=30, null=True, blank=True)
	student_contact=models.CharField(max_length=20, null=True, blank=True)
	issued_date=models.DateField(auto_now_add=True)
	book= models.ForeignKey(Book, on_delete=models.CASCADE)

	def __str__(self):
		return self.student_name
