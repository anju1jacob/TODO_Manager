from django.test import TestCase, Client
from django.urls import reverse
from todos.models import User
from .models import Project, Todo
from unittest.mock import patch

class ProjectManagerViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_index_page(self):
        response = self.client.get(reverse('index_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_page_GET(self):
        response = self.client.get(reverse('login_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_page_POST_invalid_username(self):
        response = self.client.post(reverse('login_page'), {'username': 'invaliduser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirects to login page
        self.assertRedirects(response, reverse('login_page'))

    def test_login_page_POST_invalid_password(self):
        response = self.client.post(reverse('login_page'), {'username': 'testuser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 302)  # Redirects to login page
        self.assertRedirects(response, reverse('login_page'))

    def test_login_page_POST_valid_credentials(self):
        response = self.client.post(reverse('login_page'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirects to home page
        self.assertRedirects(response, reverse('home_page'))

    def test_home_page_GET(self):
        # Test accessing the home page when logged in
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_POST(self):
        # Test creating a new project via POST request to home page
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('home_page'), {'project': 'New Project'})
        self.assertEqual(response.status_code, 200)  # Or 302 if redirecting after creating project
        self.assertTemplateUsed(response, 'home.html')  # Or check for redirect to home page

    def test_project_details_GET(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Create a project
        project = Project.objects.create(title="Test Project")

        # Send a GET request to view project details
        response = self.client.get(reverse('project_details', args=[project.id]))

        # Ensure the response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

        # Ensure the correct template is used
        self.assertTemplateUsed(response, 'project_details.html')

    def test_project_details_POST(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Create a project
        project = Project.objects.create(title="Test Project")

        # Send a POST request to add a todo item
        response = self.client.post(reverse('project_details', args=[project.id]), {'todoitem': 'Test Todo', 'description': 'Test Description'})

        # Ensure the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

        # Follow the redirect
        response = self.client.get(response.url)

        # Ensure the final response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

        # Ensure the correct template is used
        self.assertTemplateUsed(response, 'project_details.html')

    def test_update_todo_GET(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Create a project and a todo item
        project = Project.objects.create(title="Test Project")
        todo = Todo.objects.create(project=project, todoitem="Test Todo", description="Test Description")

        # Send a GET request to update the todo item
        response = self.client.get(reverse('update_todo', args=[project.id, todo.id]))

        # Ensure the response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

        # Ensure the correct template is used
        self.assertTemplateUsed(response, 'update_todo.html')

    def test_update_todo_POST(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Create a project and a todo item
        project = Project.objects.create(title="Test Project")
        todo = Todo.objects.create(project=project, todoitem="Test Todo", description="Test Description")

        # Send a POST request to update the todo item
        response = self.client.post(reverse('update_todo', args=[project.id, todo.id]), {'todoitem': 'Updated Todo', 'description': 'Updated Description', 'status': 'Complete'})

        # Ensure the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

        # Follow the redirect
        response = self.client.get(response.url)

        # Ensure the final response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

        # Ensure the correct template is used
        self.assertTemplateUsed(response, 'project_details.html')

    def test_delete_todo(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Create a project and a todo item
        project = Project.objects.create(title="Test Project")
        todo = Todo.objects.create(project=project, todoitem="Test Todo", description="Test Description")

        # Send a POST request to delete the todo item
        response = self.client.post(reverse('delete_todo', args=[project.id, todo.id]))

        # Ensure the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

        # Ensure the todo item is deleted
        self.assertFalse(Todo.objects.filter(id=todo.id).exists())

        # Follow the redirect
        response = self.client.get(response.url)

        # Ensure the final response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

        # Ensure the correct template is used
        self.assertTemplateUsed(response, 'project_details.html')

    def test_update_project_title(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Create a project
        project = Project.objects.create(title="Test Project")

        # Send a POST request to update the project title
        response = self.client.post(reverse('update_project_title', args=[project.id]), {'new_title': 'Updated Project Title'})

        # Ensure the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

        # Follow the redirect
        response = self.client.get(response.url)

        # Ensure the final response is OK (status code 200)
        self.assertEqual(response.status_code, 200)

        # Ensure the project title is updated
        updated_project = Project.objects.get(id=project.id)
        self.assertEqual(updated_project.title, 'Updated Project Title')

    

    def test_register_page_GET(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_page_POST(self):
        response = self.client.post(reverse('register'), {'first_name': 'John', 'last_name': 'Doe', 'username': 'johndoe', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirects after successful registration
        self.assertRedirects(response, reverse('register'))

    def test_user_logout(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Send a GET request to logout
        response = self.client.get(reverse('logout'))  # Corrected to 'logout'

        # Ensure the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

        # Ensure the final response is a redirect to the login page (status code 302)
        self.assertEqual(response.url, reverse('login_page'))

        # Print out the response content for debugging
        print("Response content:", response.content)

    

    @patch('todos.views.create_secret_gist')
    @patch('todos.views.save_gist_locally')
    def test_export_gist_view(self, mock_save_gist_locally, mock_create_secret_gist):
        project = Project.objects.create(title="Test Project")
        todo1 = Todo.objects.create(project=project, todoitem="Test Todo 1", description="Test Description 1")
        todo2 = Todo.objects.create(project=project, todoitem="Test Todo 2", description="Test Description 2")
        
        mock_create_secret_gist.return_value = "https://gist.github.com/testgist"
        
        response = self.client.get(reverse('export_gist', args=[project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gist created and saved locally.")
        mock_save_gist_locally.assert_called_once_with("https://gist.github.com/testgist", "Test Project")

# Add more test cases as needed
