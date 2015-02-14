from utils.models import Menu, Slider
from account.models import User
from utils.enc_dec import decrypt 

def menu(request):
	
	if request.COOKIES.has_key( '_u' ):
		user_id = request.COOKIES[ '_u' ]
		user_id = decrypt(user_id)

		try:
			User.objects.get(id=user_id)
			return {'menuitems': Menu.objects.all(), 'status':'logout'}
		except ObjectDoesNotExist:
			return {'menuitems': Menu.objects.all(), 'status':''}
	
	else:
		try:
			user_id = request.session['_u']
			user_id = decrypt(user_id)

		except Exception, e:
			return {'menuitems': Menu.objects.all(), 'status':''}
			raise

		try:
			User.objects.get(id=user_id)
			return {'menuitems': Menu.objects.all(), 'status':'logout'}
		except ObjectDoesNotExist:
			return {'menuitems': Menu.objects.all(), 'status':''}

	

def slider(request):
	return {'slideritems': Slider.objects.all()}


