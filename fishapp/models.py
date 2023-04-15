from django.db import models

# Create your models here.


class WebsiteLink(models.Model):
	link = models.CharField(max_length=100)
	
	def __str__(self):
		show = str(self.id) + " - " + self.link
		return show


class Location(models.Model):
	lat = models.CharField(max_length=100)
	lng = models.CharField(max_length=100)
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		show = str(self.id) + " - " + str(self.time)
		return show
