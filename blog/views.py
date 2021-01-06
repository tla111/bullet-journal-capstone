from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from blog.models import BlogPosts
from blog.forms import BlogPostAddForm

# Create your views here.
def home_view(request):
    blogpost = BlogPosts.objects.all()
    return render(request, 'blog_homepage.html', {'blogpost': blogpost})


def like_view(request, blogpost_id):
    post = Post.objects.filter(id=blogpost_id).first()
    post.likes += 1
    post.save()
    return redirect('blog_homepage.html')


def dislike_view(request, blogpost_id):
    post = Post.objects.filter(id=blogpost_id).first()
    post.likes += 1
    post.save()
    return redirect('blog_homepage.html')

def add_post(request):
    html = "forms/forms.html"
    if request.method == "POST":
        form = BlogPostAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BlogPosts.objects.create(
                title=data['title'],
                journal_user=request.user,
                post=data['post'],
            )
            return HttpResponseRedirect(reverse("blog_homepage"))

    form = BlogPostAddForm()
    return render(request, html, {"form": form})

@login_required
def edit_ticket(request, ticket_id):
    a = Tickets.objects.get(id=ticket_id)
    form_data = {'title': a.title, 'description': a.description}
    if request.method == "POST":
        print(request)
        form = TicketEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            a.title = data["title"]
            a.description = data['description']
            a.save()
            return HttpResponseRedirect(reverse("homepage"))
    return render(request, 'generic_form.html', {
        'form': TicketEditForm(initial=form_data),
        'title': 'Edit Ticket Screen'
    })