from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode

from django.db.models.signals import pre_save
from django.dispatch import receiver


# Not used.
def default_start_time():
	now = timezone.now()
	start = now.replace(hour=6, minute=0, second=0, microsecond=0)
	return start


class Tag(models.Model):
	"""Tag model. Many to many."""

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'
		db_table = 'tag'
		ordering = ('title',)

	title = models.CharField(max_length=100, blank=True)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True, blank=True)
	is_active = models.BooleanField(default=True)
	seo_title = models.CharField(max_length=60, blank=True, null=True)
	seo_description = models.CharField(max_length=165, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/tag/{}/'.format(self.slug)






class Post(models.Model):
	""" Post model."""

	STATUS_CHOICES = (
		('draft', 'Draft'),
		('public', 'Public'),
	)

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
		db_table = 'post'
		ordering = ('-publish',)
		get_latest_by = 'date'

	is_active = models.BooleanField(default=True)
	is_featured = models.BooleanField(default=False)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
	publish = models.DateTimeField(default=default_start_time)
	title = models.CharField(max_length=280)
	slug = models.SlugField(max_length=280, unique=True, blank=True, default='')
	content = RichTextField()
	description = models.TextField(null=True, blank=True)

	post_image = models.ImageField(upload_to='post_images/', blank=True, null=True)
	post_thumb = models.ImageField(upload_to='post_thumbs/', blank=True, null=True)
	post_image_alt = models.CharField(max_length=280, null=True, blank=True)

	author = models.ForeignKey(User, blank=True, null=True, on_delete='SET_DEFAULT')
	
	tags = models.ManyToManyField(Tag, blank=True)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)


	def save(self, *args, **kwargs):
		if not self.slug:
			base_slug = slugify(unidecode(self.title))
			new_slug = base_slug
			counter = 0
			while Post.objects.filter(slug=new_slug).exists():
				counter += 1
				new_slug = '{}-cp-{}'.format(base_slug, str(counter))
				print(new_slug)

			self.slug = new_slug


		super(Post, self).save(*args, **kwargs)



	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return '/post/{}/'.format(self.slug)


