from django.db import models

class User(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=150)
	password = models.CharField(max_length=300)
	activate = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

