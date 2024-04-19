"""
URL configuration for todo_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index_page'), 
    path('login/', views.login_page, name='login_page'), 
    path('user_logout/', views.user_logout, name='user_logout'),
    path('register/', views.register_page, name='register'),
    path('home/', views.home_page, name='home_page'),
    path('project_details/<int:project_id>/', views.project_details, name='project_details'),
    path('update_todo/<int:project_id>/<int:todo_id>/', views.update_todo, name='update_todo'),
    path('delete_todo/<int:project_id>/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('update_project_title/<int:project_id>/', views.update_project_title, name='update_project_title'),

]


