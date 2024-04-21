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
•ID: Unique identifier for the project.<br>
•Title: Title of the project.<br>
•Created Date: Date when the project was created.<br>
•Todos: List of todos associated with the project.<br>
<h4>Todo</h4>
•ID: Unique identifier for the todo.<br>
•Description: Description of the todo task.<br>
•Status: Status of the todo (Pending or Complete).<br>
•Created Date: Date when the todo was created.<br>
•Updated Date: Date when the todo was last updated.
