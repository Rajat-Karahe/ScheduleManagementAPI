from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Event(models.Model):
	title = models.CharField(max_length=100)
	event_date = models.DateField() 
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		ordering = ('event_date',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('event-detail', kwargs={'pk': self.pk})
    		
    	