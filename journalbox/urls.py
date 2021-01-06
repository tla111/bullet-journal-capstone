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
<<<<<<< HEAD
from profile_journal.views import JournalPageView
from blog import views
=======
from profile_journal.views import JournalPageView, AddAssignmentView, AssignmentDetailView, LessonAssignmentView, ActivityAssignmentView, QuizAssignmentView, AssessmentAssignmentView, CompletedAssignmentView, DeleteAssignmentView
>>>>>>> 2ac35f40c27d5c3ca773cafc27a01526ed9fbfec

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('journal/', JournalPageView.as_view(), name='journal'),
    path('add_assignment/', AddAssignmentView.as_view()),
    path('assignment_detail/<int:assignment_id>/', AssignmentDetailView.as_view()),
    path('lesson_assignment/<int:assignment_id>/', LessonAssignmentView.as_view()),
    path('activity_assignment/<int:assignment_id>/', ActivityAssignmentView.as_view()),
    path('quiz_assignment/<int:assignment_id>/', QuizAssignmentView.as_view()),
    path('assessment_assignment/<int:assignment_id>/', AssessmentAssignmentView.as_view()),
    path('completed_assignment/<int:assignment_id>/', CompletedAssignmentView.as_view()),
    path('delete_assignment/<int:assignment_id>/',
         DeleteAssignmentView.as_view()),
    path('admin/', admin.site.urls),
    path('blog_homepage/', views.home_view, name='blog_homepage' ),
    path('blogpost_submit/', views.add_post,),
]
