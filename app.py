# This is a to do application made using flask and sqlalchemy

from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy

# if you want to make this a static app, that stores data in memory,
# comment out the lines 12, 13, 15, 19, 20, 21, 27, 28, 29
# uncomment line 17, 18
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

# for database definition
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# todos = ["Learn Flask", "Setup venv", "Build a cool app"]

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_text = db.Column(db.String(100), index = True)

    def __rep__(self):
        return '<Task %r>' % self.id

class ToDoForm(FlaskForm):
    todo = StringField("todo")
    submit = SubmitField("Add Todo")

# Creation of the database tables within the application context.
# with app.app_context():
#     db.create_all()

@app.route('/', methods=["GET", "POST"])
def index():
    # return "Hello World"
    if request.method == "POST":
        if 'todo' in request.form:
            # todos.append(request.form['todo'])
            todo_content = request.form['todo']
            new_todo = ToDo(todo_text = todo_content)

            try:
                db.session.add(new_todo)
                db.session.commit()
                return redirect('/')
            except:
                return 'There was an error while adding the todo'
    else:
        todos = ToDo.query.all()
        return render_template("index.html", todos=todos, template_form=ToDoForm())

@app.route('/delete/<int:id>')
def delete(id):
    todo_to_delete = ToDo.query.get_or_404(id)
    try:
        db.session.delete(todo_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error while deleting that to do item'

if __name__ == '__main__':
    app.run(debug=True)