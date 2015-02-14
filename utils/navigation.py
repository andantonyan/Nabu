from django.http import Http404
from utils.models import Menu, Submenu
from django.utils.importlib import import_module
from django.core.exceptions import ObjectDoesNotExist

def menu(request, menu):
	menu = menu.lower().strip()
	try:
		menu = Menu.objects.get(slug=menu)
		app = menu.app
		action = menu.action
		if app=='doc':
			return getattr(import_module("%s.views" % app),action)(request, menu.id, submenu=False)
		else:
			return getattr(import_module("%s.views" % app),action)(request)
	except ObjectDoesNotExist:
		raise Http404


def submenu(request, menu, submenu):
	menu = menu.lower().strip()
	submenu = submenu.lower().strip()

	try:
		menu = Menu.objects.get(slug=menu)
		submenuobject = menu.submenu_set.all()

		try:
			submenuobject = menu.submenu_set.all()
			submenuobject = submenuobject.get(slug=submenu)
			app = submenuobject.app
			action = submenuobject.action
			if app=='doc':
				return getattr(import_module("%s.views" % app),action)(request, submenuobject.id, submenu=True)
			
			else:
				return getattr(import_module("%s.views" % app),action)(request)
		except ObjectDoesNotExist:
			raise Http404


		return HttpResponse(submenuobject.id)
	except ObjectDoesNotExist:
		raise Http404

