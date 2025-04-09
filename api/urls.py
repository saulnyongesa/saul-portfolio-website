from django.urls import  path
from api import views

urlpatterns = [
    path('user/', views.get_user, name='user-url'),
    path('projects/', views.get_projects, name='projects-url'),
    path('projects/create/', views.create_project, name='create-project-url'),
    path('projects/update/<int:project_id>/', views.update_project, name='update-project-url'), 
    path('projects/delete/<int:project_id>/', views.delete_project, name='delete-project-url'),
    path('projects/<int:project_id>/', views.get_project, name='project-url'),

    
    path('skills/', views.get_skills, name='skills-url'),
    path('skills/create/', views.create_skill, name='create-skill-url'),
    path('skills/update/<int:skill_id>/', views.update_skill, name='update-skill-url'),
    path('skills/delete/<int:skill_id>/', views.delete_skill, name='delete-skill-url'),
    path('skills/<int:skill_id>/', views.get_skill, name='skill-url'),

    path('emails/', views.get_emails, name='emails-url'),
    path('emails/create/', views.create_email, name='create-email-url'),
    path('emails/<int:email_id>/', views.get_email, name='email-url'),
    path('emails/delete/<int:email_id>/', views.delete_email, name='delete-email-url'),
]
