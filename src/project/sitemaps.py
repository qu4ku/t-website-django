from django.contrib.sitemaps import Sitemap
from core.models import Post
from django.urls import reverse


class PostSitemap(Sitemap):
	changefreq = 'daily'
	priority = 0.5
	protocol = 'https'

	def items(self):
		return Post.published.all()

	def lastmod(self, obj):
		return obj.modified


class HomeSitemap(Sitemap):
	priority = 0.8
	changefreq = 'daily'
	protocol = 'https'

	def items(self):
		return ['home']

	def location(self, item):
		return reverse(item)


