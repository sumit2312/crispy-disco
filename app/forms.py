from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from app.models import Comment, Request
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']
	helper = FormHelper()
	helper.form_method = 'POST'
	helper.add_input(Submit('Comment', 'Comment', css_class='btn-primary'))


class LoginForm(forms.Form):
	username = forms.CharField(max_length=30, help_text='Enter your Username', required=True)
	password = forms.CharField(widget=forms.PasswordInput, help_text='Password', required=True)
	helper = FormHelper()
	helper.form_method = 'POST'
	#helper.add_input(Submit('login', 'login', css_class='btn-primary'))

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		if not user:
			raise forms.ValidationError("Sorry, that login was invalid. Please try again.")

class SearchForm(forms.Form):
	name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Search'}))
	helper = FormHelper()
	helper.form_method = 'POST'
	helper.add_input(Submit('Search', 'Search', css_class='btn-primary'))

class RequestForm(ModelForm):
	class Meta:
		model = Request
		fields = ['problem']
	helper = FormHelper()
	helper.form_method = 'POST'
	helper.add_input(Submit('Share', 'Share', css_class='btn-primary'))

