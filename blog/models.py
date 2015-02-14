# -*- coding: utf-8 -*-
from django.db import models
from account.models import User

class Article(models.Model):
	author = models.ForeignKey(User)
	# title = models.CharField(max_length=300)
	body = models.TextField()
	created = models.DateTimeField(auto_now=True)


	def __unicode__(self):
		return str(self.created)

	class Meta:
		ordering = ['-created']

class Comment(models.Model):
	author = models.ForeignKey(User)
	article = models.ForeignKey(Article)
	body = models.TextField()
	created = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['created']

	def __unicode__(self):
		return str(self.created)