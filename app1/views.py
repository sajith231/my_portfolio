from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request,'app1/index.html')

def about(request):
    return render(request, 'app1/about.html')


def education(request):
    return render(request, 'app1/education.html')



def skills(request):
    return render(request, 'app1/skills.html')






from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:  # Check if user is valid
            login(request, user)
            return redirect('skills')  # Redirect to skills page after successful login
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'app1/login.html')  # Your login page template





from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            messages.success(request, 'Project created successfully!')
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'app1/create_project.html', {'form': form})

@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('projects')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'app1/edit_project.html', {'form': form, 'project': project})

@login_required
def delete_project(request, project_id):
    # Check if user is the project owner or is a superuser
    project = get_object_or_404(Project, id=project_id)
    
    # Only allow deletion if user is project owner or a superuser
    if request.user != project.user and not request.user.is_superuser:
        messages.error(request, 'You do not have permission to delete this project.')
        return redirect('projects')
    
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('projects')
    
    return render(request, 'app1/delete_project.html', {'project': project})

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'app1/projects.html', {'projects': projects})

def logout_view(request):
    logout(request)  # This will log the user out
    return redirect('home')  # Redirect to home or any page you want after logout







from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Skill
from .forms import SkillForm

@login_required
def add_skill(request):
    if not request.user.is_superuser:
        messages.error(request, 'Only superusers can add skills.')
        return redirect('skills')
        
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('add_skill')  # Redirect to refresh the list

    else:
        form = SkillForm()

    # Fetch all skills from the database
    skills = Skill.objects.all()

    return render(request, 'app1/add_skill.html', {'form': form, 'skills': skills})




from django.contrib.auth.decorators import login_required
from .models import Skill

# views.py
def skills(request):
    # If user is authenticated, show their skills
    if request.user.is_authenticated:
        coding_skills = Skill.objects.filter(category='coding', user=request.user)
        professional_skills = Skill.objects.filter(category='professional', user=request.user)
    else:
        # For non-authenticated users, show all skills without user filter
        coding_skills = Skill.objects.filter(category='coding')
        professional_skills = Skill.objects.filter(category='professional')
    
    return render(request, 'app1/skills.html', {
        'coding_skills': coding_skills,
        'professional_skills': professional_skills,
    })



from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Skill

@login_required
def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id, user=request.user)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully!')
    return redirect('add_skill')