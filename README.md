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
Clone the repository: git clone <repository-url>
Navigate to the project directory: cd todo_manager
Set up a virtual environment (optional but recommended): python -m venv venv
Activate the virtual environment:
For Windows: venv\Scripts\activate
For macOS/Linux: source venv/bin/activate
Install dependencies: pip install -r requirements.txt
Create a .env file in the root directory and configure environment variables (e.g., database connection, GitHub token).
Apply database migrations: python manage.py migrate
Run Instructions
Start the development server: python manage.py runserver
Open your web browser and navigate to http://127.0.0.1:8000/.
Test Instructions
Run tests: python manage.py test
View test coverage: coverage run --source='.' manage.py test && coverage report
Usage
Sign up or log in with your credentials.
Create a new project and start adding todos.
Manage todos within each project (add, edit, update, mark as complete).
Export project summary as a secret gist on GitHub.
Technologies Used
Python
Django
Django Rest Framework
PostgreSQL (or any preferred database)
HTML/CSS
JavaScript (optional for frontend enhancements)
Contributors
John Doe (john@example.com)
Jane Smith (jane@example.com)
