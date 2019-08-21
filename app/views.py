from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Comment
from .forms import LoginForm, CommentForm, SearchForm, RequestForm

def index(request):
	if request.method == 'POST':
		title = request.POST['title']
		questions = Question.objects.all().filter(title__startswith=title)
	else:
		questions = Question.objects.all().order_by('-pub_date')
	user = request.user
	return render(request, 'index.html', {'questions' : questions, 'user' : user})

def showDetails(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	comments = Comment.objects.all().filter(question=question)
	user = request.user
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.cleaned_data['comment']
			Comment.objects.create(comment=comment, name=request.user, question=question)
			return HttpResponseRedirect(reverse('showDetails', 
				kwargs={'question_id':question_id}))
	else:
		form = CommentForm()
		return render(request, 'showDetails.html', {'question' : question, 'comments'
			: comments, 'form' : form, 'user' : user})

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('login'))
		return render(request, 'register.html', {'form' : form})
	else:
		form = UserCreationForm()
		return render(request, "register.html", {'form' : form})

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			auth_login(request, user)
			return HttpResponseRedirect(reverse('index'))
		else:
			return render(request, 'login.html', {'form' : form})
	else:
		form = LoginForm()
		return render(request, "login.html", {'form' : form})

def logoutView(request):
	logout(request)
	return HttpResponseRedirect('/')

def share(request):
	if request.method == 'POST':
		form = RequestForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('index'))
		else:
			return render(request, 'request.html', {'form' : form})
	else:
		form = RequestForm()
		return render(request, 'request.html', {'form' : form})





