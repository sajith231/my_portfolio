from django.urls import path
from . import views 
from .views import delete_skill
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('login/', views.login_view, name='login'),
    path('projects/', views.projects, name='projects'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/edit/<int:project_id>/', views.edit_project, name='edit_project'),
    path('projects/delete/<int:project_id>/', views.delete_project, name='delete_project'),
    path('logout/', views.logout_view, name='logout'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('delete_skill/<int:skill_id>/', delete_skill, name='delete_skill'),
]