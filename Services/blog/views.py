from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import BlogPost
from .forms import CreateBlogPostForm, UpdateBlogPostForm
from operator import attrgetter
from Services import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 

# Функция отображения постов, а также пагинация
@login_required(login_url='login')
def home_screen_view(request):
    
    # context = {}
    blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_update'), reverse=True)
    # context['blog_posts'] = blog_posts
    paginator = Paginator(blog_posts, 2)
    page = request.GET.get('page')
    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        blog_posts = paginator.page(1)
    except EmptyPage:
        blog_posts = paginator.page(paginator.num_pages)
    return render(request, "blog/blog.html", context={'blog_posts' : blog_posts})

# Функция создания данных о постах
def create_blog_view(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreateBlogPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = User.objects.filter(email=request.user.email).first()
		obj.author = author
		obj.save()
		form = CreateBlogPostForm()

	context['form'] = form
		
	return render(request, 'blog/create_blog.html', context)

# Функция просмотра детальной информации о постах
def detail_blog_view(request, slug):
	
	context = {}
	blog_post = get_object_or_404(BlogPost, slug=slug)
	context['blog_post'] = blog_post

	return render(request, 'blog/detail_blog.html', context)

# Функция изменения данных о постах
def edit_blog_view(request, slug):
	
	context = {}
	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	blog_post = get_object_or_404(BlogPost, slug=slug)
	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Успешно изменено"
			blog_post = obj
	
	form = UpdateBlogPostForm(
			initial={
					"title": blog_post.title, 
					"body": blog_post.body,
				}
			)
	context['form'] = form

	return render(request, 'blog/edit_blog.html', context)


