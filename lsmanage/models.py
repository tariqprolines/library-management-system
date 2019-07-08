from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
	id= models.AutoField(primary_key=True)
	call_no= models.CharField(max_length=20, null=True, blank= True, unique=True)
	name=models.CharField(max_length=30, null=True, blank= True)
	author=models.CharField(max_length=30, null=True, blank=True)
	publisher=models.CharField(max_length=50, null=True, blank=True)
	quantity=models.IntegerField(default=0)
	issued=models.IntegerField(default=0)
	created_date=models.DateField(auto_now_add=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE)  

	def __str__(self):
		return self.name

