"""journalbox URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from profile_journal.views import JournalPageView
from blog import views

from profile_journal.views import JournalPageView, AddAssignmentView, AssignmentDetailView, LessonAssignmentView, ActivityAssignmentView, QuizAssignmentView, AssessmentAssignmentView, CompletedAssignmentView, DeleteAssignmentView


from authentication.views import home
# >>>>>>> 80c5cbb4bdbea7a49a5c9e58846f70f2fb80d7fa

from profile_journal.views import JournalPageView, AddAssignmentView, AssignmentDetailView, LessonAssignmentView, ActivityAssignmentView, QuizAssignmentView, AssessmentAssignmentView, CompletedAssignmentView, DeleteAssignmentView, AddReflectionView
from authentication.views import home, index, register, logout_view
from blog import views
from django.conf.urls import url
from django.views.static import serve 
from django.conf import settings

# >>>>>>> 7ce28d065b921d4f481895d355dd87fc0ada2327
urlpatterns = [
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('auth/', include('authentication.urls')),
    path('journal/', JournalPageView.as_view(), name='journal'),
    path('add_assignment/', AddAssignmentView.as_view()),
    path('add_reflection/', AddReflectionView.as_view()),
    path('assignment_detail/<int:assignment_id>/', AssignmentDetailView.as_view()),
    path('lesson_assignment/<int:assignment_id>/', LessonAssignmentView.as_view()),
    path('activity_assignment/<int:assignment_id>/', ActivityAssignmentView.as_view()),
    path('quiz_assignment/<int:assignment_id>/', QuizAssignmentView.as_view()),
    path('assessment_assignment/<int:assignment_id>/', AssessmentAssignmentView.as_view()),
    path('completed_assignment/<int:assignment_id>/', CompletedAssignmentView.as_view()),
    path('delete_assignment/<int:assignment_id>/',
         DeleteAssignmentView.as_view()),
    path('admin/', admin.site.urls),
    # path('login/', authviews.index, name="login"),
    # path('register/', authviews.register, name="register"),git
    # path('logout/', authviews.logout_view, name="logout"),
    path('', home, name="home"),
    path('login/', index, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout_view, name="logout"),
    path('', home, name="home"),
    path('blog/', views.blog_index, name="blog"),
    path('create_post/', views.create_post, name="create_post"),
    path('search/', views.search, name="search"),
    path('edit_post/<int:id>/', views.edit_post, name="edit_post"),
    path('delete_post/<int:id>/', views.delete_post, name="delete_post"),
    path('comment/<int:id>/', views.comment, name="comment"),
    path('article/<int:id>/', views.article, name="article"),

    path('upvote/<int:id>/', views.up_vote, name="upvote"),
    path('downvote/<int:id>/', views.down_vote, name="downvote"),

]
