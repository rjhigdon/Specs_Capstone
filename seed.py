import os  
import model
import server
from crud import create_user, create_project, create_task
from faker import Faker
from random import Random, randint, choice

random = Random()
fake=Faker()


os.system("dropdb myapp")
os.system("createdb myapp")

model.connect_to_db(server.app)

with server.app.app_context():
    model.db.create_all()
#Creates 10 users
    for _ in range(10):
        username = fake.first_name()
        password = fake.text(10)

        user = create_user(username, password)
        model.db.session.add(user)
 
#Creates 100 Projects randomly assigned to a user        
    for _ in range (30):
        project_name = fake.text(10)
        project_description = fake.text(100)
        user_id = randint(1,10)
        
        project = create_project(project_name, project_description, user_id)
        model.db.session.add(project)

#Creates 1000 tasks randomly assigned to a project and status        
    for _ in range (1000):
        
        statuses = ['Backlog', 'To-Do', 'In-Progress', 'Completed']
        
        task_name = fake.text(10)
        task_description = fake.text(100)
        status = random.choice(statuses)
        project_id = randint(1,30)
        
        task = create_task(task_name, task_description, status, project_id)
        model.db.session.add(task)

    model.db.session.commit()
    