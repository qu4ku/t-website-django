from django.urls import path

from . import views


urlpatterns = [
	path('', views.home_view, name='home'),
	path('artykuly/', views.articles_view, name='articles'),
	path('artykuly/<slug:slug>/', views.post_view, name='post'),
]