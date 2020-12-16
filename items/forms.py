from django import forms
from django.contrib.auth.models import User

class SignUp(forms.ModelForm):
	username= forms.CharField(widget=forms.TextInput(),max_length =30,required=True,)
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget = forms.PasswordInput(),label="Confirm Password")
	class Meta:
		model = User
		fields = ['username', 'password', 'confirm_password']

	def clean(self):
		super(SignUp, self).clean()
		password= self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password and password != confirm_password:
			self._errors['password'] =self.error_class(
				['Passwords don\'t match']
				)
		return self.cleaned_data
