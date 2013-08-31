__author__ = 'tejawork'

from django.db import models


class Address(models.Model):
	street_name = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=20)

	class Meta:
		app_label = "shopping"