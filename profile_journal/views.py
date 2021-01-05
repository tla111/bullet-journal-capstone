from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
# Create your views here.


class JournalPageView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "journal_profile.html")
