__author__ = 'tejawork'

from django.db import models

class Rating(models.Model):

	num_of_stars = models.SmallIntegerField()
	description = models.TextField(max_length=10000)

	class Meta():
		app_label = "shopping"