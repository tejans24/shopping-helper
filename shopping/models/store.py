__author__ = 'tejawork'

from address import Address
from rating import Rating
from django.db import models

class Store(models.Model):

	name = models.CharField(max_length=50, unique=True)
	description = models.TextField(blank=True)
	url = models.CharField(max_length=500, unique=True)
	main_category = models.CharField(max_length=100)
	address = models.ForeignKey(Address)
	ratings = models.ManyToManyField(Rating)

	class Meta:
		app_label = "shopping"