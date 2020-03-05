# Note-Taking-API
The Note Taking API for a web application based on Django.

Modules required to be installed in your Python Virtual Environment:
1. Django(version 3.0) - pip install django==3.0.0
2. Django Rest Framework - pip install djangorestframework

To create superuser:
1. Navigate to project/
2. Run the command: python manage.py createsuperuser
3. Set username and password

Steps to run the server:
1. Navigate to project/
2. Run the server with the following command: python manage.py runserver
3. Open the web broswer and go to localhost:8000/article/
4. The default username and password is 'admin'

The API performs the following calls:
1. GET /article/view - Displays the id, Username, Note text, Created Date, Last Updated Date for all the notes in the application.
2. GET /article/view/{id no} - Displays the id, Username, Note text, Created Date, Last Updated Date for the note with the given id.
3. POST /article/view/ - Adds a new note.
4. PUT /article/view/{id no} - For editing details of the note including username, note text and last updated date.
5. DELETE /article/view/{id no} - For deleting a particular note with the given id no.
  
