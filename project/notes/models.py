from django.db import models

# Create your models here.
import datetime

class Note(models.Model):
	username = models.CharField(max_length=100)
	note_text = models.TextField(max_length=40000)
	created_date = models.DateField(("Created Date"),auto_now_add=True)
	last_updated_date = models.DateField(("Updated Date"), default=datetime.date.today)

	def __str__(self):
		return self.username