from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import User, Project, Todo
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.

def index_page(request):
    return render(request,'index.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
         
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
         
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/home/')
     
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login_page')  # Redirect to the login page after logout

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
         
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
         
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
         
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
         
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')
    
    return render(request, 'register.html')

@login_required
def home_page(request):
    if request.method=='POST':
        projectname=request.POST['project']
        projects=Project.objects.create(title=projectname)
        projects.save()
        projects = Project.objects.all()  # Retrieve all projects
        return render(request, 'home.html', {'projects': projects}) 
    else:
        projects = Project.objects.all()
        return render(request, 'home.html', {'projects': projects})
    

@login_required
def project_details(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    todos = project.todos.all()

    if request.method == 'POST':
        todoitem = request.POST.get('todoitem')
        description = request.POST.get('description')
        Todo.objects.create(project=project, todoitem=todoitem, description=description)

        return redirect('project_details', project_id=project_id)
    else:
        return render(request, 'project_details.html', {'project': project, 'todos': todos})

@login_required    
def update_todo(request, project_id, todo_id):
    project = get_object_or_404(Project, id=project_id)
    todo = get_object_or_404(Todo, id=todo_id)
    todos = project.todos.all()
    if request.method == 'POST':
        todoitem=request.POST.get('todoitem')
        description = request.POST.get('description')
        status = request.POST.get('status')
        
        # Update todo fields
        todo.todoitem =todoitem
        todo.description = description
        todo.status = status
        todo.save()

        return redirect('project_details', project_id=project_id)
    else:
        return render(request, 'update_todo.html', {'project': project, 'todo': todo, 'todos': todos})
    
@login_required
def delete_todo(request, project_id, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('project_details', project_id=project_id)

def update_project_title(request, project_id):
    if request.method == 'POST':
        new_title = request.POST.get('new_title')
        project = get_object_or_404(Project, id=project_id)
        project.title = new_title
        project.save()
        return redirect('home_page')
    else:
        # Handle GET request if needed
        pass

@csrf_exempt
def create_gist(request):
    if request.method == "POST":
        access_token = "YOUR_GITHUB_ACCESS_TOKEN"  # Replace with your actual GitHub access token
        data = request.json()
        project_title = data.get("projectTitle")
        project_summary = data.get("projectSummary")
        filename = f"{project_title}.md"
        gist_id = create_gist(access_token, filename, project_summary)
        return JsonResponse({"gistId": gist_id})
    return JsonResponse({"error": "Method not allowed"}, status=405)

def download_gist(request):
    gist_id = request.GET.get("gist_id")
    access_token = "YOUR_GITHUB_ACCESS_TOKEN"  # Replace with your actual GitHub access token
    output_filename = f"exported_project_summary.md"
    download_gist(access_token, gist_id, output_filename)
    # Here you can return a response to indicate that the download is successful 