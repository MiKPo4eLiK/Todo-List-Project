Todo-List-Project

This application is a simple yet effective tool for managing a To-Do List. 
It allows users to create, view, update, and delete tasks, as well as mark them as completed. 
The application is built on the Django framework and demonstrates the basic principles of CRUD operations.

Functionality:
Create tasks: Add new tasks with content, tags and due date.

  -- View tasks: List of all tasks with the ability to filter them by tags.

  -- Update tasks: Edit existing tasks, change their content, tags or status.

  -- Delete tasks: Ability to delete tasks that are no longer needed.

  -- Completed status: Mark tasks as completed or incomplete.

Technologies Used

  -- Server: Django (Python)

  -- Interface: HTML, CSS

Requirements:
To run this application locally, you need to have the following components installed:

  -- Python (version 3.6 or higher)

  -- pip (Python package manager)

Installation and Startup:
Follow the following steps to set up and run the project on your local machine:

  -- Clone the repository:

  git clone https://github.com/your-username/repository-name.git
  cd repository-name

  -- Replace your-username and repository-name with your own.

  -- Create and activate a virtual environment:

  python -m venv venv
  # For Windows
  venv\Scripts\activate
  # For macOS/Linux
  source venv/bin/activate

Install dependencies:

  -- pip install -r requirements.txt

Perform database migrations:

  -- python manage.py migrate

Start the local server:

  -- python manage.py runserver

Open the application in a browser:

  -- Go to http://127.0.0.1:8000/.

To login, you can use the following test credentials:

  -- Username: Admin888

  -- Password: User258312341258
