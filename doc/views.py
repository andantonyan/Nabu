from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from utils.models import Menu, Submenu
from account.models import User
from utils.enc_dec import decrypt

# Create your views here.
def show(request, pk, submenu):
	# return HttpResponse(pk)
	if submenu:
		menu = Submenu.objects.get(id=pk)

		return render(request, 'doc/show.html', {'html':menu.html, 'slider': menu.show_slider, 'title': menu.title})
	else:
		menu = Menu.objects.get(id=pk)


		return render(request, 'doc/show.html', {'html':menu.html, 'slider': menu.show_slider, 'title': menu.title})
	
