from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from .models import Assignments
from .forms import AddAssignment
# Create your views here.


class JournalPageView(LoginRequiredMixin, View):
    def get(self, request):
        kenzie_assignments = Assignments.objects.filter(user_created=request.user)
        return render(request, "journal_profile.html", {'assignments': kenzie_assignments} )



class AddAssignmentView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddAssignment()
        return render(request, 'forms/generic_form.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
                form = AddAssignment(request.POST)
                if form.is_valid():
                    data = form.cleaned_data
                    Assignments.objects.create(
                        title=data['title'],
                        description=data['description'],
                        assignment_type='New',
                        user_created=request.user,
                    )
        return HttpResponseRedirect(reverse('journal'))