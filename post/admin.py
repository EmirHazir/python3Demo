from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'publishedDate']
    list_display_links = ['publishedDate']
    list_filter = ['publishedDate']
    search_fields =['title', 'content']
    list_editable = ['title']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)