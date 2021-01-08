from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogModel
from .forms import BlogForm
from django.contrib import messages


def blog_index(request):
    posts = BlogModel.objects.order_by('-list_date').all()
    context = {
        'posts': posts
    }
    return render(request, "blog/index.html", context)


def create_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BlogModel.objects.create(
                title=data['title'],
                body=data['body'],
                tags=data['tags'],
                author=request.user
            )
            return redirect('blog')
        else:
            messages.error(request, 'Body Text Exceeds 300 Characters')
            return redirect('create_post')
    form = BlogForm()
    context = {
        'title': 'Create Post',
        "BTN_Text": 'Post it!',
        'form': form
    }
    return render(request, 'forms/form.html', context)


def search(request):
    search_list = BlogModel.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            print(keywords)
            search_list = search_list.filter(tags__icontains=keywords)

    context = {
        "results": search_list,
        "keywords": keywords

    }
    return render(request, 'blog/results.html', context)


def edit_post(request, id):
    post = get_object_or_404(BlogModel, id=id)
    if request.method == "POST":
        edit = BlogForm(request.POST)
        if edit.is_valid():
            data = edit.cleaned_data
            post.title = data['title']
            post.body = data['body']
            post.tags = data['tags']
            post.save()
            return redirect('blog')

    form = BlogForm(instance=post)
    context = {
        'form': form,
        'BTN_Text': 'Up Date Post'
    }

    return render(request, 'forms/form.html', context)


def delete_post(request, id):
    BlogModel.objects.filter(id=id).delete()
    return redirect('blog')
