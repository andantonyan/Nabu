import os
from uuid import uuid4
from utils.enc_dec import decrypt
from account.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper


def check_user(request):
    
    if request.COOKIES.has_key( '_u' ):
        user_id = request.COOKIES[ '_u' ]
        user_id = decrypt(user_id)

        try:
            User.objects.get(id=user_id)
            return user_id
        except ObjectDoesNotExist:
            raise Http404
    
    else:
        try:
            user_id = request.session['_u']
            user_id = decrypt(user_id)

        except Exception, e:
            raise Http404

        try:
            User.objects.get(id=user_id)
            return user_id
        except ObjectDoesNotExist:
            raise Http404
