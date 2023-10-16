import os  
from random import choice, randint

import model
import server
from crud import create_user, create_project, create_task

os.system("dropdb KanbanApp")
os.system("createdb KanbanApp")

model.connect_to_db(server.app)

with model.session.app.app_context():
    model.db.create_all()
    
    for n in range(10):
        username = f"user{randint(100,1000)}"
        password = "test_pw"

    user = create_user(username, password)
    
    