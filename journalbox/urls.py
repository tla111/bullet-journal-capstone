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
from profile_journal.views import JournalPageView, AddAssignmentView, AssignmentDetailView, LessonAssignmentView, ActivityAssignmentView, QuizAssignmentView, AssessmentAssignmentView, CompletedAssignmentView, DeleteAssignmentView, AddReflectionView
from authentication.views import home, index, register, logout_view
from blog import views
from django.conf.urls import url
from django.views.static import serve 
from django.conf import settings

urlpatterns = [
    # url(r'^media/(?P.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
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
    path('login/', index, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout_view, name="logout"),
    path('', home, name="home"),
    path('blog/', views.blog_index, name="blog"),
    path('create_post/', views.create_post, name="create_post"),
    path('search/', views.search, name="search"),
    path('edit_post/<int:id>/', views.edit_post, name="edit_post"),
    path('delete_post/<int:id>/', views.delete_post, name="delete_post"),
]
