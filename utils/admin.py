from django.contrib import admin
from .models import Menu, Submenu, Slider, Mail
# Register your models here.


# class SubmenuInline(admin.TabularInline):
# 	model = Submenu
# 	extra = 3

# class MenuAdmin(admin.ModelAdmin):
# 	inlines = [SubmenuInline]

class SliderAdmin(admin.ModelAdmin):
	list_display = ('photo', 'html','show')
	search_fields = ['name']


	def photo(self, obj):
		return '<img src="/%s" width="150" height="100" />' % obj.picture
	photo.allow_tags = True

class MenuAdmin(admin.ModelAdmin):
	list_display = ('name', 'show')
	search_fields = ['name']


class SubmenuAdmin(admin.ModelAdmin):
	list_display = ('name', 'menu', 'show')
	search_fields = ['name']

admin.site.register(Menu, MenuAdmin)
admin.site.register(Submenu, SubmenuAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Mail)


