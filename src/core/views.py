from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, get_list_or_404
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
		post_list = Post.published.filter(
			Q(title__icontains=query) |
			Q(content__contains=query) | 
			Q(description__contains=query) |
			Q(author__contains=query)
		).distinct().filter(is_active=True)
	else:
		post_list = Post.published.filter(is_active=True)

	paginator = Paginator(post_list, 9)
	page = request.GET.get('page')
	posts = paginator.get_page(page)




	template = 'blog.html'
	context = {
		'posts': posts,
	}

	return render(request, template, context)


def post_view(request, slug):
	
	post = get_object_or_404(Post, slug=slug, is_active=True)
	
	template = 'blog-post.html'
	context = {'post': post}

	return render(request, template, context)








