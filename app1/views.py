from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,'app1/index.html')

def about(request):
    return render(request, 'app1/about.html')


def education(request):
    return render(request, 'app1/education.html')



def skills(request):
    return render(request, 'app1/skills.html')