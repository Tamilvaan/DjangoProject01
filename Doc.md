      School Student Management System (CRUD) — Django Project Documentation

Overview

The School Student Management System is a web application built using Django.
It allows users to add, view, update, and delete student details through a simple web UI.
All data is stored in a database and displayed dynamically on the web pages.


| Technology           | Version | Description          |
| -------------------- |---------| -------------------- |
| Python               | 3.13    | Programming language |
| Django               | 5.2.7   | Web framework        |
| SQLite               | Default | Database             |
| HTML, CSS, Bootstrap | —       | Frontend UI          |


Features

✅ Add new student details
✅ View all students in a table
✅ Edit existing student information
✅ Delete student records
✅ Data stored in the database
✅ Simple and user-friendly web interface


Project Structure 

DjangoProject/
|   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Frontend/
│   ├── migrations/
│   ├── templates/
│   
│           ├── base.html
│           ├── student_add.html
│           └── student_list.html
└── manage.py
|
|
|___Inventory.py
|   |
|   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
    └── admin.py

Install Django
pip install django

Create Django Project
django-admin startproject DjangoProject

Create a Django Apps
python manage.py startapp Inventory
python manage.py startapp Frontend

Model Fields Explanation(Inventory.models.py)

Field Name	        Field Type	Description
first_name	        CharField	Stores the student’s first name (max 100 characters).
last_name	        CharField	Stores the student’s last name (max 100 characters).
email	            EmailField	Stores the student’s email. It must be unique — no two students can have the same email.
enrollment_number	CharField	Unique identification number for each student (like a roll number).
course	            CharField	The name of the course or program the student is enrolled in (e.g., BSc Computer Science).
date_joined	        DateField	Automatically stores the date when the record was created (using auto_now_add=True).

Views (Inventory.views.py)
 1. Add Student (Student_add)
 Description:
 Displays a student registration form to the user.
 When the form is submitted (POST method), it validates and saves the data to the database.
 Uses the StudentForm (ModelForm) to handle input validation.
 Template:
 student_add.html → Contains HTML form fields for adding student details.
 
 2. List Students (student_list)
 Description:
 Fetches all student records from the database using Student.objects.all().
 Sends the list to the student_list.html template for display.
 Typically includes "Edit" and "Delete" buttons for each record.
 Template:
 student_list.html → Displays all student entries in a table.
 
 3. Delete Student (delete)
 Description:
 Locates a student by their unique id.
 Deletes the student record from the database.
 Redirects the user back to the student list page.
 Template:
 Usually triggered via a “Delete” button in student_list.html.

 4. Update Student (update)
 Description:
 Retrieves a student record by id.
 Displays the existing data in the same form used for adding (student_add.html).
 If the form is submitted and valid, updates the record in the database.
 Redirects back to the student list page after updating.
 Template:
 student_add.html → Used for both creating and updating records.
  
User Interface (Templates)
 base.html
 This HTML file serves as the base template for all pages in the Django Student Management System.
 It provides a consistent layout — including navigation, footer, and background styling — that is inherited by other templates using Django’s {% extends %} and {% block content %} tags.
 
 student_add.html
 This template provides the User Interface (UI) for adding new student details or updating existing student information in the database.
 It uses Django’s ModelForm to automatically generate form fields from the Student model.
 
 student_list.html
 This template displays a list of all students stored in the database.
 It shows student details in a tabular format with options to update or delete each record.
 It uses the Student model data passed from the Django view (student_list view function).
 
 Urls

 DjangoProject urls(urls.py)
 path('inventory/', include('Inventory.urls'))

 Inventory urls(urls.py)
 urlpatterns =[
    path('student/add/',Student_add),
    path('student/list/',student_list),
    path('student/list/delete/<int:id>',delete,name="student_delete"),
    path('student/list/update/<int:id>',update,name="student_update"),
]

 Run the Project
 python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver
 
 
 
 
 