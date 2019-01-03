from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
from .models import Post

def home_view(request):
	template = 'home.html'
	is_blog = True
	context = {
		'blog': is_blog,
	}

	return render(request, template, context)


def blog_view(request):
	query = request.GET.get('q')
	if query:
		post_list = Post.objects.filter(
			Q(title__icontains=query) |
			Q(content__contains=query) | 
			Q(description__contains=query) |
			Q(author__contains=query)
		).distinct().filter(is_active=True)
	else:
		post_list = Post.objects.filter(is_active=True)

	paginator = Paginator(post_list, 9)
	page = request.GET.get('page')
	posts = paginator.get_page(page)




	template = 'blog.html'
	context = {
		'posts': posts,
	}

	return render(request, template, context)