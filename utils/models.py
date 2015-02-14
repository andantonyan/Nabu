from django.db import models
from .functions import path_and_rename




class Menu(models.Model):
	title = models.CharField(max_length=150, help_text="Page Title", blank=True)
	name = models.CharField(max_length=150, help_text="Must Be Displayed In Menu")
	slug = models.CharField(max_length=150, blank=True, help_text="Example. python-tuturial(lowercase)")
	# name_parameter = models.CharField(max_length=150, help_text="Example. python_tuturial")
	app = models.CharField(max_length=150, help_text="For HTML documents write 'doc'")
	action = models.CharField(max_length=150, help_text="For HTML documents write 'show'")
	show = models.BooleanField(default=True, help_text="Displayed or Hide in Menu")
	order = models.IntegerField(help_text="Ordering Example. '0, 1, 2, 3'")
	show_slider = models.BooleanField(default=False, help_text="Displayed or Hide Slider")
	html = models.TextField(blank=True, help_text="insert HTML")
	
	class Meta:
		ordering = ['order']

	def __unicode__(self):
		return self.name

class Submenu(models.Model):
	menu = models.ForeignKey(Menu, help_text="Select Perent")
	title = models.CharField(max_length=150, help_text="Page Title", blank=True)
	name = models.CharField(max_length=150, help_text="Must Be Displayed In Menu")
	slug = models.CharField(max_length=150, blank=True, help_text="Example. python-tuturial(lowercase)k")
	# name_parameter = models.CharField(max_length=150, help_text="Example. python_tuturial")
	app = models.CharField(max_length=150, help_text="For HTML documents write 'doc'")
	action = models.CharField(max_length=150, help_text="For HTML documents write 'show'")
	show = models.BooleanField(default=True, help_text="Displayed or Hide in Menu")
	order = models.IntegerField(help_text="Ordering Example. '0, 1, 2, 3'")
	show_slider = models.BooleanField(default=False, help_text="Displayed or Hide Slider")
	html = models.TextField(blank=True, help_text="insert HTML")


	class Meta:
		ordering = ['order']

	def __unicode__(self):
		return self.name

class Slider(models.Model):
	name = models.CharField(max_length=150, help_text="Picture Name")
	alt = models.CharField(max_length=150, help_text="Picture Alt Name")
	show = models.BooleanField(default=True, help_text="Displayed or Hide")
	order = models.IntegerField(help_text="Ordering Example. '0, 1, 2, 3'")
	picture = models.FileField(upload_to=path_and_rename('static/upload/slider'))
	show_html = models.BooleanField(default=False, help_text="Displayed or Hide Slider Text")
	html = models.TextField(blank=True, help_text="insert HTML")

	class Meta:
		ordering = ['order']

	def __unicode__(self):
		return self.name

class Mail(models.Model):
	account_activate_subject = models.CharField(max_length=150, blank=True, help_text="Mail Subject")
	account_activate_body = models.TextField(blank=True, help_text="Mail Body")

	def __unicode__(self):
		return 'Mail Content'

