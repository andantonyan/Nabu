# -*- coding: utf-8 -*-
from django.core.mail import EmailMessage
from utils.models import Mail


def account_activate(email, key, domain):
	try:
		mail = Mail.objects.get(id=1)
		subject = mail.account_activate_subject
		message = mail.account_activate_body
		message = message.replace('[domain]', domain).replace('[key]', key)
		email = EmailMessage(subject, message, to=[email])
		email.content_subtype = "html"
		email.send()
		return True

	except Exception, e:
		return False
		raise e
