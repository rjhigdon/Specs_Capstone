import os  
from random import choice, randint

import model
import server
from crud import create_user

if os.system("dropdb --if-exists KanbanApp") == 0:
    print("Database 'KanbanApp' dropped successfully")
else:
    print("Database 'KanbanApp' does not exist")
os.system("createdb KanbanApp")

model.connect_to_db(server.app)

with server.app.app_context():
    model.db.create_all()
    
    for n in range(10):
        username = f"user{randint(100,1000)}"
        password = "test_pw"

    user = create_user(username, password)
    model.db.session.add(user)
    