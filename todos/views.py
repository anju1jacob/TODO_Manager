from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import User, Project, Todo
from django.contrib import messages
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import requests
import os
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
    print("Logging out user:", request.user.username)
    logout(request)
    print("User logged out")
    return redirect('login_page')



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
        # After creating the todo, fetch all todos again
        todos = project.todos.all()
        return HttpResponseRedirect(request.path_info)

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



def create_secret_gist(title, content, token):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "files": {
            f"{title}.md": {
                "content": content
            }
        },
        "public": False
    }
    response = requests.post("https://api.github.com/gists", headers=headers, json=data)
    if response.status_code == 201:
        return response.json()["html_url"]
    else:
        return None

def save_gist_locally(gist_url, project_title):
    gist_id = gist_url.split('/')[-1]
    download_url = f"https://gist.github.com/{gist_id}/download"
    response = requests.get(download_url)
    with open(f"{project_title}.md", "wb") as f:
        f.write(response.content)

def export_gist_view(request, project_id):
    project = Project.objects.get(id=project_id)
    pending_todos = project.todos.filter(status='Pending').values_list('todoitem', flat=True)
    completed_todos = project.todos.filter(status='Complete').values_list('todoitem', flat=True)
    total_todos = project.todos.count()
    completed_count = project.todos.filter(status='Complete').count()

    # Generate project summary in Markdown format
    summary = f"# {project.title}\n\nSummary: {completed_count}/{total_todos} completed.\n\n## Pending Todos\n"
    for todo in pending_todos:
        summary += f"- [ ] {todo}\n"
    summary += "\n## Completed Todos\n"
    for todo in completed_todos:
        summary += f"- [x] {todo}\n"

    # Create secret gist
    github_token = os.environ.get('GITHUB_TOKEN')
    gist_url = create_secret_gist(project.title, summary, github_token)
    
    # Save gist locally
    if gist_url:
        save_gist_locally(gist_url, project.title)
        return HttpResponse("Gist created and saved locally.")
    else:
        return HttpResponse("Failed to create gist.")