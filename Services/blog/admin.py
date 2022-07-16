from django.contrib import admin

from blog.models import BlogPost

# admin.site.register(BlogPost)
@admin.register(BlogPost)
class Admin(admin.ModelAdmin):
    fields = ('title', 'body', 'author', 'slug', )
    list_display = ('title', 'date_published', 'date_update', )
    list_filter = ('title',)

