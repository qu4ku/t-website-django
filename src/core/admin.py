from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):

	class Meta:
		model = Post

	list_display = ['title', 'status', 'is_active']
	list_editable = ['is_active']
	list_filter = ['is_active', 'tags']
	search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)