from app import db, ToDo, app
from flask_sqlalchemy import SQLAlchemy

# commented after first commit 
# first_todo = ToDo(todo_text="Learn Flask")

# with app.app_context():
#     db.session.add(first_todo)
#     db.session.commit()

# with app.app_context():
#     allTodos = ToDo.query.all()
#     print(allTodos[0].todo_text)
#     print(allTodos[1].todo_text)
