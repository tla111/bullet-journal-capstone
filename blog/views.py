
from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from blog.models import BlogModel, CommentModel
from blog.forms import BlogForm, CommentForm


# Create your views here.


def like_view(request,id):
    post = BlogModel.objects.filter(id=BlogModel_id).first()
    post.likes += 1
    post.save()
    return redirect('blog_homepage.html')


def dislike_view(request, blogpost_id):
    post = BlogModel.objects.filter(id=BlogModel_id).first()
    post.likes += 1
    post.save()
    return redirect('blog_homepage.html')

# def add_post(request):
#     html = "forms/forms.html"
#     if request.method == "POST":
#         form = BlogPostAddForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             BlogPosts.objects.create(
#                 title=data['title'],
#                 journal_user=request.user,
#                 post=data['post'],
#             )
#             return HttpResponseRedirect(reverse("blog_homepage"))
#
#     form = BlogPostAddForm()
#     return render(request, html, {"form": form})
#
# @login_required
# def edit_ticket(request, ticket_id):
#     a = Tickets.objects.get(id=ticket_id)
#     form_data = {'title': a.title, 'description': a.description}
#     if request.method == "POST":
#         print(request)
#         form = TicketEditForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             a.title = data["title"]
#             a.description = data['description']
#             a.save()
#             return HttpResponseRedirect(reverse("homepage"))
#     return render(request, 'generic_form.html', {
#         'form': TicketEditForm(initial=form_data),
#         'title': 'Edit Ticket Screen'
#     })

# def all_blogs(request):
#     blogs = Blog.objects.order_by('-date')
#     return render(request, 'forms/blogs.html', {'blogs': blogs})
# >>>>>>> 80c5cbb4bdbea7a49a5c9e58846f70f2fb80d7fa

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


# def create_comment(request):
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             BlogModel.objects.create(
#                 title=data['title'],
#                 body=data['body'],
#                 tags=data['tags'],
#                 author=request.user
#             )
#             return redirect('blog')
#         else:
#             messages.error(request, 'Body Text Exceeds 300 Characters')
#             return redirect('create_comment')
#     form = BlogForm()
#     context = {
#         'title': 'Create Comment',
#         "BTN_Text": 'Post it!',
#         'form': form
#     }
#     return render(request, 'forms/form.html', context)