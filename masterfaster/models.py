from django.contrib.auth.models import AbstractUser

from django.db import models
from django.utils import timezone
import datetime

class User(AbstractUser):
	username=models.CharField(primary_key=True, unique=True, max_length=50)
	email = models.EmailField(max_length=200)
	password = models.CharField(max_length=200)
	credit_card_number = models.CharField(max_length=50, null=True)
	credit_card_exp_date_month = models.CharField(max_length=10, null=True)
	credit_card_exp_date_year = models.CharField(max_length=10, null=True)
	credit_card_csv = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.username

class Address(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=50, null=True)
	city = models.CharField(max_length=20, null=True)
	state = models.CharField(max_length=50, null=True)
	zipcode = models.IntegerField(default=00000, null=True)
	country = models.CharField(max_length=50, null=True)

	class Meta:
	    abstract = True

class Billing(Address):
	def __str__(self):
		return self.user

class Shipping(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=50, null=True, blank=True)
	city = models.CharField(max_length=20, null=True, blank=True)
	state = models.CharField(max_length=50, null=True, blank=True)
	zipcode = models.IntegerField(default=00000, null=True, blank=True)
	country = models.CharField(max_length=50, null=True, blank=True)
	same_as_billing=models.BooleanField(default=True)
	def __str__(self):
		return self.user