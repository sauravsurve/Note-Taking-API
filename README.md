# Note-Taking-API
The Note Taking API for a web application based on Django.

Modules required to be installed:
1. Django(version 3.0) - pip install django==3.0.0
2. Django Rest Framework - pip install djangorestframework


The following API performs the following calls:
1. GET /article/view - Displays the id, Username, Note text, Created Date, Last Updated Date for all the notes in the application.
2. GET /article/view/{id no} - Displays the id, Username, Note text, Created Date, Last Updated Date for the note with the given id.
3. POST /article/view/ - Adds a new note.
4. PUT /article/view/{id no} - For editing details of the note including username, note text and last updated date.
5. DELETE /article/view/{id no} - For deleting a particular note with the given id no.
  
