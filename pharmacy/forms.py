from django import forms
class FormUser(forms.Form):
 firstName = forms.CharField (max_length=30)
 lastName = forms.CharField (max_length=30)
 login = forms.CharField (max_length=10)
 password = forms.CharField (widget=forms.PasswordInput)
 confirm = forms.CharField (widget=forms.PasswordInput)
 email = forms.EmailField (max_length=200)





class formConnection(forms.Form):
 login = forms.CharField (max_length=10)
 password = forms.CharField (widget=forms.PasswordInput)