from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView,DeleteView,UpdateView,DetailView
from .models import Profile
from django.contrib.auth.decorators import login_required


class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'account/detail.html'
    fields = ['fname', 'mname', 'lname', 'studno','section' ]

class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'account/delete.html'
    fields = ['fname', 'mname', 'lname', 'studno','section' ]


class ProfileCreateView(LoginRequiredMixin,CreateView):
    model = Profile
    template_name = 'account/create.html'
    fields = ['fname', 'mname', 'lname', 'studno','section' ]

class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = Profile
    template_name = 'account/update.html'
    fields = ['fname', 'mname', 'lname', 'studno','section' ]

class ProfileDeleteView(LoginRequiredMixin,DeleteView):
    model = Profile
    template_name = 'account/Delete.html'
    fields = ['fname', 'mname', 'lname', 'studno','section' ]



@login_required
def profile_queryset(request):
    profile_list = ''
    if request.GET:
        query = request.GET.get('search_name')
        queryset = []
        queries = query.split(" ")
        for q in queries:
            profiles = Profile.objects.filter(
                Q(fname__icontains=q) |
                Q(mname__icontains=q) |
                Q(lname__icontains=q) |
                Q(studno__icontains=q) |
                Q(section__icontains=q) 
            ).distinct()

            for profile in profiles:
                queryset.append(profile)
        profile_list =  list(set(queryset))


    return render(request, 'account/index.html', {'profile_list':profile_list})

