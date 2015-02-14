# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import LoginForm, RegistrationForm, UpdateNameForm, UpdatePasswordForm
from .models import User
from django.core.exceptions import ObjectDoesNotExist
from utils.enc_dec import encrypt, decrypt
from django.forms.util import ErrorList
from utils.send_mail import account_activate
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from utils.functions import check_user
min_len = 6


# def login(request):
# 	form = LoginForm()
# 	return render(request, 'account/login.html', {'form': form})


def login(request):

	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			try:
				email = request.POST['email']
				email = email.strip()
				password = request.POST['password']
				password = password.strip()
				user = User.objects.get(email=email)

				if user.activate:

					if decrypt(user.password) != password:
						form._errors["password"] = ErrorList([u'Ծածկագիրը սխալ է'])
						return render(request, 'account/login.html', {'form': form})
						raise

					try:
						request.POST['remember']
						response = HttpResponseRedirect('/')
						response.set_cookie('_u', encrypt(user.id), max_age = 30*24*60*60)						
						return response
					except Exception, e:
						request.session['_u'] = encrypt(user.id)
						request.session.set_expiry(0)
						return HttpResponseRedirect('/')
						# response = HttpResponseRedirect('/')
						# response.set_cookie('_u', encrypt(user.id))						
						# return response	


					
				else:
					form._errors["email"] = ErrorList([u'Հաշիվը ակտիվացված չէ'])
					return render(request, 'account/login.html', {'form': form})
					raise


			except ObjectDoesNotExist:
				form._errors["email"] = ErrorList([u'Նշված էլեկրոնային հասցեով օգտատեր չկա'])
				return render(request, 'account/login.html', {'form': form})
				raise
		else:
			return render(request, 'account/login.html', {'form': form})			
	else:
		form = LoginForm()
		return render(request, 'account/login.html', {'form': form})


def registration(request):

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			try:
				email = request.POST['email']
				email = email.strip()
				user = User.objects.get(email=email)
				form._errors["email"] = ErrorList([u'Նշված էլեկրոնային հասցեն զբաղված է'])
				return render(request, 'account/registration.html', {'form': form})
				raise
			except ObjectDoesNotExist:
				password = request.POST['password']
				password = password.strip()
				if len(password)<min_len:
					form._errors["password"] = ErrorList([u'Գաղտնաբառը պետք է գերազանցի 6 նիշը'])
					return render(request, 'account/registration.html', {'form': form})
					raise					
				else:
					name = request.POST['name']
					name = name.strip()
					email = request.POST['email']
					email = email.strip()
					password = request.POST['password']
					password = password.strip()
					password = encrypt(password)
					User.objects.create(
						name=name,
						password=password,
						email=email
					)

					if(account_activate(email, encrypt(email), request.META['HTTP_HOST'])):
						return HttpResponseRedirect('/thanks')

					

		return render(request, 'account/registration.html', {'form': form})

	else:
		form = RegistrationForm()
		return render(request, 'account/registration.html', {'form': form})


def logout(request):
	response = HttpResponseRedirect('/')
	response.delete_cookie('_u')
	request.session.flush()	
	return response


def thanks(request):
	return render(request, 'account/thanks.html')



def activate(request, email):
	email = email.strip()
	email = decrypt(email)
	try:
		user = User.objects.get(email=email)
		if user.activate:
			raise Http404
		else:
			user.activate = True
			user.save()
			return render(request, 'account/activate.html')
	except ObjectDoesNotExist:
		raise Http404


def settings(request):
	user = User.objects.get(id = check_user(request))
	nameform = UpdateNameForm()
	passwordform = UpdatePasswordForm()





	if request.method == 'POST':
		nameform = UpdateNameForm(request.POST)
		passwordform = UpdatePasswordForm(request.POST)
		errors = False
		success = False


		if 'name' in request.POST:

			if nameform.is_valid():
				name = request.POST['name']
				name = name.strip()

				if(len(name) != 0):
					user.name = name
					user.save()
					# if(len())
					nameform = UpdateNameForm()
					success = u'Անունը թարմացված է'
					return render(request, 'account/settings.html', {'user':user,'nameform':nameform, 'passwordform':passwordform, 'success':success})
				else:

					errors = u'Լրացրեք պարտադիր դաշտերը'
					nameform = UpdateNameForm()
					return render(request, 'account/settings.html', {'user':user,'nameform':nameform, 'passwordform':passwordform, 'errors':errors})
			else:
				errors = u'Լրացրեք պարտադիր դաշտերը'
				nameform = UpdateNameForm()
				return render(request, 'account/settings.html', {'user':user,'nameform':nameform, 'passwordform':passwordform})
		
		elif 'password' in request.POST and 'new_password' in request.POST:
			if passwordform.is_valid():

				password = request.POST['password']
				password = password.strip()
				# password = password

				new_password = request.POST['new_password']
				new_password = new_password.strip()


				if decrypt(user.password) == password:

					if len(new_password)<min_len:
						errors = u'Գաղտնաբառը պետք է գերազանցի 6 նիշը'
						return render(request, 'account/settings.html', {'user':user,'nameform':nameform, 'passwordform':passwordform, 'errors':errors})

					else:
						user.password = encrypt(new_password)
						user.save()
						success = u'Գաղտնաբառը թարմացված է'
						return render(request, 'account/settings.html', {'user':user,'nameform':nameform, 'passwordform':passwordform, 'success':success})

				else:
					errors = u'Ծածկագիրը սխալ է'
					# passw = encrypt(new_password)
					return render(request, 'account/settings.html', {'user':user,'nameform':nameform, 'passwordform':passwordform, 'errors':errors})		
			else:

				return render(request, 'account/settings.html', {'user':user,'nameform':nameform, 'passwordform':passwordform, 'errors':errors})

		else:
			return render(request, 'account/settings.html', {'user':user,'nameform':nameform, 'passwordform':passwordform, 'errors':errors})
	else:
		return render(request, 'account/settings.html', {'user':user,'nameform':nameform, 'passwordform':passwordform})







	
	


