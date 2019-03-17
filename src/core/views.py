from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Post

def home_view(request):
	template = 'home.html'
	context = {
	}

	return render(request, template, context)


def articles_view(request):
	ARTICLES_PER_PAGE = 3

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

	paginator = Paginator(post_list, ARTICLES_PER_PAGE)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	template = 'articles.html'
	context = {
		'posts': posts,
	}

	return render(request, template, context)


def post_view(request, slug):
	posts = Post.published.filter(is_active=True)
	post = get_object_or_404(Post, slug=slug, is_active=True)

	idx = list(posts).index(post)
	try:
		prev_post = posts[idx - 1]
	except IndexError:
		prev_post = None
	try:
		next_post = posts[idx + 1]
	except IndexError:
		next_post = None

	template = 'post.html'
	context = {
		'post': post,
		'prev_post': prev_post,
		'next_post': next_post,
	}

	return render(request, template, context)








