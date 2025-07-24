from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from jobs.models import Job, Application, Profile

@login_required
def dashboard(request):
    user = request.user 
    context = {}
    if user.role == 'employer':
        posted_jobs = Job.objects.filter(employer=user)
        applications = Application.objects.filter(job__in=posted_jobs)
        context.update({
            'posted_jobs': posted_jobs,
            'applications': applications
        })
    else: 
        applied_jobs = Job.objects.filter(application__user=user)
        context.update({
            'applied_jobs': applied_jobs
        })
    return render(request, 'users/dashboard.html', context)

@login_required
def profile_view(request):
    user = request.user
    
    if user.role == 'job_seeker':
        profile, created = Profile.objects.get_or_create(user=user)
    
    return render(request, 'users/profile.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('home')
    return render(request, 'users/delete_account.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
