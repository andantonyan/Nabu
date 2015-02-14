# -*- coding: utf-8 -*-
from django import forms

my_default_errors = {
    'required': u'Լրացրեք պարտադիր դաշտերը',
    'invalid': u'Մուտքագրեք ճիշտ տվյալ'
}



# login form
class LoginForm(forms.Form):
    email = forms.EmailField(
        label=u'Էլեկտոնային հասցե',
        error_messages=my_default_errors,
        widget=forms.EmailInput(attrs={
    		'autofocus':"", 
    		'required':"", 
    		'placeholder':"Էլեկտոնային հասցե", 
    		'class':"form-control"}
    	))
    password = forms.CharField(
        label=u'Գաղտնաբառ', 
        error_messages=my_default_errors,
        widget=forms.PasswordInput(attrs={
    		'autofocus':"", 
    		'required':"", 
    		'placeholder':"Գաղտնաբառ", 
    		'class':"form-control"}
    	))

    remember = forms.BooleanField(initial=True, label=u'Մնալ ցանցում', required=False)


# registration form
class RegistrationForm(forms.Form):
    email = forms.EmailField(
        label=u'Էլեկտոնային հասցե',
        error_messages=my_default_errors,
        widget=forms.EmailInput(attrs={
    		'autofocus':"", 
    		'required':"", 
    		'placeholder':"Էլեկտոնային հասցե", 
    		'class':"form-control"}
    	))

    name = forms.CharField(label=u'Անուն',
        error_messages=my_default_errors,
        widget=forms.TextInput(attrs={
    		'autofocus':"", 
    		'required':"", 
    		'placeholder':"Անուն", 
    		'class':"form-control"}
    	))

    password = forms.CharField(label=u'Գաղտնաբառ', 
        error_messages=my_default_errors,
        widget=forms.PasswordInput(attrs={
    		'autofocus':"", 
    		'required':"", 
    		'placeholder':"Գաղտնաբառ", 
    		'class':"form-control"}
    	))


# user name update form
class UpdateNameForm(forms.Form):
    name = forms.CharField(label=u'Անուն',
        error_messages=my_default_errors,
        # required=False,
        widget=forms.TextInput(attrs={
            'autofocus':"", 
            'required':"", 
            'placeholder':"Անուն", 
            'class':"form-control"}
        ))


# password update form
class UpdatePasswordForm(forms.Form):

    password = forms.CharField(label=u'Հին գաղտնաբառ', 
        error_messages=my_default_errors,
        # required=False,
        widget=forms.PasswordInput(attrs={
            'autofocus':"", 
            'required':"", 
            'placeholder':"Հին գաղտնաբառ", 
            'class':"form-control"}
        ))

    new_password = forms.CharField(label=u'Նոր գաղտնաբառ', 
        error_messages=my_default_errors,
        # required=False,
        widget=forms.PasswordInput(attrs={
            'autofocus':"", 
            'required':"", 
            'placeholder':"Նոր գաղտնաբառ", 
            'class':"form-control"}
        ))