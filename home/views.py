from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from utils.enc_dec import encrypt, decrypt
# from django.core.exceptions import ObjectDoesNotExist

# from utils.models import Menu
# from account.models import User
# Create your views here.

def index(request):
	# menuitems = Menu.objects.all()
	# if request.COOKIES.has_key( '_u' ):
	# 	user_id = request.COOKIES[ '_u' ]
	# 	user_id = decrypt(user_id)

	# 	try:
	# 		User.objects.get(id=user_id)
	# 		return render(request, 'home/index.html', {'status': 'logout'})
	# 	except ObjectDoesNotExist:
	# 		return render(request, 'home/index.html', {'status': ''})

	return render(request, 'home/index.html')

def lessons(request):
	return HttpResponse('leesons')