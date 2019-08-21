from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.showDetails, name='showDetails'),
    path('register',views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logoutView, name='logoutView'),
    path('request', views.share, name='share'),
]