from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogModel, CommentModel
from journaluser.models import BulletJournalUser
from .forms import BlogForm, CommentForm
from django.contrib import messages
from django.db.models import Count

def blog_index(request):
    results = BlogModel.objects.order_by('-list_date').all()
    # toptags = BlogModel.objects.values_list('tags').annotate(tag_count=Count('tags')).order_by('-tag_count')
    # tags = [char for char in toptags if char.isalnum()]
    # tags = "".join(tags)
    # print(results.tags)
    context = {
        'results': results,
        # 'toptags': toptags,
    }
    return render(request, "blog/index.html", context)


def create_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            BlogModel.objects.create(
                title=data['title'],
                body=data['body'],
                tags=data['tags'],
                blog_image=data['blog_image'],
                author=request.user
            )
            return redirect('blog')
        else:
            messages.error(request, 'Body Text Exceeds 300 Characters')
            return redirect('create_post')
    form = BlogForm()
    context = {
        'title': 'Celebrate an Achievement',
        "BTN_Text": 'Post it!',
        'form': form
    }
    return render(request, 'forms/form.html', context)
    

def search(request):
    search_tag = BlogModel.objects.order_by('-list_date')

    if 'tags' in request.GET:
        tags = request.GET['tags']
        if tags:
            search_tag = search_tag.filter(tags__icontains=tags)

    context = {
        "results": search_tag
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
        'BTN_Text': 'Update Post'
    }

    return render(request, 'forms/form.html', context)


def delete_post(request, id):
    BlogModel.objects.filter(id=id).delete()
    return redirect('blog')


def article(request, id):
    results = BlogModel.objects.get(id=id)
    comments = CommentModel.objects.filter(
        post=results.id).order_by('-created_date')

    context = {
        'results': results,
        'comments': comments
    }

    return render(request, 'blog/article.html', context)


def comment(request, id):
    post = get_object_or_404(BlogModel, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CommentModel.objects.create(
                post=post,
                context=data['context'],
                author=request.user
            )
            return redirect(f'/article/{id}')
        else:
            messages.error(request, 'Comment Text Exceeds 280 Characters')
            return redirect(f'/article/{id}')
    form = CommentForm()
    context = {
        'title': 'Celebrate an Achievement',
        "BTN_Text": 'Post it!',
        'form': form
    }
    return render(request, 'forms/form.html', context)



# def up_vote(request, id):
#     post = BlogModel.objects.get(id=id)
#     post.likes += 1
#     post.save()
#     return redirect('article', id=id)


# def down_vote(request, id):
#     post = BlogModel.objects.get(id=id)
#     post.dislikes += 1
#     post.save()
#     return redirect('article', id=id)


def up_vote(request, id):
    post = BlogModel.objects.get(id=id)
    post.likes += 1
    post.save()
    return redirect(f'/article/{id}')

# def comment_likes(request, id):
#     post = CommentModel.objects.get(id=id)
#     post.likes += 1
#     post.save()
#     return redirect('article', id=id)


# def comment_likes(request, id):
#     post = CommentModel.objects.get(id=id)
#     post.likes += 1
#     post.save()
#     return redirect('article', id=id)

# def down_vote(request, id):
#     post = BlogModel.objects.get(id=id)
#     post.dislikes += 1
#     post.save()
#     return redirect(f'/article/{id}')
