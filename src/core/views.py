from django.shortcuts import render


def home_view(request):
	template = 'home.html'
	is_blog = False
	context = {
		'blog': is_blog,
	}

	return render(request, template, context)



