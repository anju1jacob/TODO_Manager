# Todo Manager Application

# Description
The Todo Manager Application is a web-based tool developed using Django that allows users to manage their tasks and projects efficiently. With this application, users can create new projects, manage todos within each project (add, edit, update, mark as complete), and export project summaries as secret gists on GitHub.
# Features
• Basic Auth for user login <br>
• Users can create a new project with a unique title.<br>
• Users can add, edit, update, and mark todos as complete within each project.<br>
• Users can export the project summary in markdown format as a secret gist on GitHub.
# Schema
<h4>Project</h4>
• ID: Unique identifier for the project.<br>
• Title: Title of the project.<br>
• Created Date: Date when the project was created.<br>
• Todos: List of todos associated with the project.<br>
<h4>Todo</h4>
• ID: Unique identifier for the todo.<br>
• Description: Description of the todo task.<br>
• Status: Status of the todo (Pending or Complete).<br>
• Created Date: Date when the todo was created.<br>
• Updated Date: Date when the todo was last updated.

# GITHUB_TOKEN  creation
1. Sign in to GitHub:<br>
&nbsp;&nbsp;&nbsp;  Sign in to your GitHub account if you haven't already. You'll need to have an existing GitHub account to create a token.<br>
2. Access Personal Access Tokens Page:<br>
• Click on your profile picture at the top-right corner of GitHub.<br>
• From the dropdown menu, select "Settings".<br>
• In the left sidebar, click on "Developer settings".<br>
• From the expanded sidebar, click on "Personal access tokens" (classic) .<br>
3. Generate a New Token:<br>
• Click on the "Generate new token" button.<br>
• You may need to re-enter your password for authentication.<br>
• Provide a meaningful note for the token to remind you of its purpose.<br>
• Select the scopes (permissions) needed for your token. For this Django project, you may only need the gist scope if you're creating gists.<br>
• Click on the "Generate token" button at the bottom of the page.<br>
4. Copy the Token:<br>
• Once the token is generated, GitHub will display it on the screen. Important: Copy the token immediately as you won't be able to see it again. Store it securely, as it provides access to your GitHub account.
# Gist Creation
set up the GITHUB_TOKEN environment variable on machine before running the project. <br>
 &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; Windows:   &nbsp;&nbsp; <b> set GITHUB_TOKEN=your_github_token_here </b> ( Using Command Prompt) <br>
 &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; Linux/macOS : &nbsp;&nbsp; <b> export GITHUB_TOKEN=your_github_token_here </b>

# Setup Instructions
• Clone the repository: &nbsp;&nbsp;  <b>git clone repository-url</b><br>
• Navigate to the project directory:&nbsp;&nbsp;  <b> cd todo_manager</b><br>
• Set up a virtual environment (optional but recommended): <br>
   &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;<b> 1. virtualenv venv</b> (install virtual enviornment)<br>
    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;    <b> 2. python -m virtualenv venv </b>(create virtual enviornment)<br></p>
• Activate the virtual environment:<br>
    &nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp;  <b> For Windows: venv\Scripts\activate</b><br>
     &nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp; <b> For macOS/Linux: source venv/bin/activate</b><br>
• Install dependencies:&nbsp; &nbsp; <b>pip install django</b><br>
• Apply database migrations:<br>
    &nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp;  <b>python manage.py makemigrations</b><br>
     &nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp; <b>python manage.py migrate</b><br>
# Run Instructions
• Start the development server:   <b> python manage.py runserver</b><br>
• Open your web browser and navigate to  http://127.0.0.1:8000/.<br>
# Test Instructions
• Run tests:&nbsp;&nbsp;  <b>  python manage.py test</b><br>
• View test coverage: <br>
    &nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp; <b>  1. pip install coverage</b> (install this  package to view the test coverage)<br>
     &nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp; <b>2. coverage run --source='.' manage.py test && coverage report</b><br>
# Usage
• Sign up or log in with your credentials.<br>
• Create a new project and start adding todos.<br>
• Manage todos within each project (add, edit, update, mark as complete).<br>
• Export project summary as a secret gist on GitHub.
## Technology Stack
* Frontend: HTML/CSS, JavaScript, Bootstrap<br>
* Backend: Python<br>
* Web Framework: Django<br>
* Database: Sqlite3<br>

# Contributors
Anju Jacob &nbsp;&nbsp; (jacob.anju98@gmail.com)
