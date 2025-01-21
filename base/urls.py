from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home" ),
    path('about/', views.about, name = "about" ),
    path('skills/', views.skills, name = "skills" ),
    path('projects/', views.projects, name = "projects" ),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('certifications/', views.certification_list, name='certification_list'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
    path('contact/', views.contact, name = "contact" ),
]