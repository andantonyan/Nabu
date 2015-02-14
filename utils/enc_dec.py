from django.core import signing

def encrypt(value):
	return signing.dumps(value)
	

def decrypt(value):
	return signing.loads(value)