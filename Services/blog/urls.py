from django.urls import path
from blog.views import(

    create_blog_view,
    detail_blog_view,
    edit_blog_view,
    home_screen_view,
)

app_name = 'blog'

urlpatterns = [
    path('blog', home_screen_view, name='blog'),
    path('create/', create_blog_view, name="create"),
    path('<slug>/', detail_blog_view, name="detail"),
    path('<slug>/edit', edit_blog_view, name="edit"),
]
