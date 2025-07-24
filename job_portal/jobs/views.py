from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import JobForm, ApplicationForm, ProfileForm
from .models import Job, Application, Category
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

@login_required
def job_post(request):
    if request.user.role != 'employer':
        messages.error(request, "Only employers can post jobs.")
        return redirect('home')
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user 
            job.save()
            messages.success(request, "Job posted successfully!")
            return redirect('home')
    else:
        form = JobForm()
        
    return render(request, 'jobs/job_post.html', {'form': form})

@login_required
def job_applications_view(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user)
    applications = Application.objects.filter(job=job)
    
    if request.method == 'POST':
        app_id = request.POST.get('app_id')
        new_status = request.POST.get('status')
        app = get_object_or_404(Application, id=app_id)
        app.status = new_status
        app.save()
        messages.success(request, 'Application status updated.')
    
    return render(request, 'jobs/job_applications.html', {'job': job, 'applications': applications})

def job_list(request):
    query = request.GET.get('q')
    location = request.GET.get('location')
    category_filter = request.GET.get('category')
    
    jobs = Job.objects.all()
    categories = Category.objects.all()
    
    if query:
        jobs = jobs.filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    if location:
        jobs = jobs.filter(location__icontains=location)

    if category_filter:
        jobs = jobs.filter(category=category_filter)
        
    if category_id := request.GET.get("category"):
        jobs = jobs.filter(category_id=category_id)
        
    paginator = Paginator(jobs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'jobs': page_obj,
        'categories': categories,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
        'search': query,
        'location': location
    }
    
    return render(request, 'jobs/job_list.html', context)

@login_required
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    # Only seekers can apply
    can_apply = request.user.role == 'job_seeker'
    
    if request.method == 'POST' and can_apply:
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user 
            application.job = job 
            application.save()
            messages.success(request, 'You have successfully applied!')
            return redirect('job_detail', job_id=job.id)
    else:
        form = ApplicationForm()
        
    context = {
        'job': job,
        'form': form,
        'can_apply': can_apply
    }
    return render(request, 'jobs/job_detail.html', context)

@login_required
def edit_profile(request):
    profile = request.user.profile
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'jobs/edit_profile.html', {'form': form})
