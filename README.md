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

# Setup Instructions
• Clone the repository:   git clone repository-url<br>
• Navigate to the project directory:   cd todo_manager<br>
• Set up a virtual environment (optional but recommended): <br>
   &nbsp;&nbsp;&nbsp; &nbsp;1. virtualenv venv (install virtual enviornment)<br>
    &nbsp;&nbsp;&nbsp; &nbsp;     2. python -m virtualenv venv (create virtual enviornment)<br></p>
• Activate the virtual environment:<br>
    &nbsp;&nbsp;&nbsp; &nbsp;   For Windows: venv\Scripts\activate<br>
     &nbsp;&nbsp;&nbsp; &nbsp;  For macOS/Linux: source venv/bin/activate<br>
• Install dependencies: pip install django<br>
• Apply database migrations:<br>
    &nbsp;&nbsp;&nbsp; &nbsp;   python manage.py makemigrations<br>
     &nbsp;&nbsp;&nbsp; &nbsp;  python manage.py migrate<br>
# Run Instructions
• Start the development server:    python manage.py runserver<br>
• Open your web browser and navigate to  http://127.0.0.1:8000/.<br>
# Test Instructions
• Run tests:  python manage.py test<br>
• View test coverage: <br>
    &nbsp;&nbsp;&nbsp; &nbsp;   1. pip install coverage (install this  package to view the test coverage)<br>
     &nbsp;&nbsp;&nbsp; &nbsp;  2. coverage run --source='.' manage.py test && coverage report<br>
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
Anju Jacob(jacob.anju98@gmail.com)
