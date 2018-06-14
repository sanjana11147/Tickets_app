from django.db import models

class Ticket(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		"""tickss"""
		return self.title
