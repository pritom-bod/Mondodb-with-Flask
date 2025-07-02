# Mondodb-with-Flask
Overview
________________

This project is a simple blog management backend and frontend interface built using Flask and MongoDB. It demonstrates how to perform CRUD operations on Authors and Posts with a template-based user interface. The project uses MongoDB for data storage and Flask Blueprints for organized route management.


Features
____________________________

1.Author creation, viewing, updating, and deletion

2.Post creation, viewing, updating, and deletion

3.Template-based interface using Jinja2

4.MongoDB as the database backend

5.Bootstrap for simple, responsive design

6.Well-structured Flask Blueprint architecture


Project Structure:
_______________________

project/
│
├── app.py
├── requirements.txt
├── utils/
│   └── db.py
├── routes/
│   ├── author_routes.py
│   └── post_routes.py
└── templates/
    ├── base.html
    ├── authors/
    │   ├── list.html
    │   ├── create.html
    │   └── edit.html
    └── posts/
        ├── list.html
        ├── create.html
        └── edit.html


Prerequisites:
______________________

Python 3.10 or higher

MongoDB running on localhost:27017

Postman (optional, for testing API requests)

Installation:
_______________________

Clone the repository
git clone <your-repository-url>
cd project
Create and activate a virtual environment

python -m venv env
env\Scripts\activate   (on Windows)
source env/bin/activate  (on Mac/Linux)


Install dependencies
_________________________

pip install -r requirements.txt
Ensure MongoDB is running locally.

Running the Project
To start the Flask server, run:

python app.py
Then open your browser and navigate to:

http://127.0.0.1:5000

This will redirect automatically to the Author listing page.

