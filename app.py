import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Correction de l'URI de la base de données pour SQLAlchemy
database_url = os.getenv('DATABASE_URL')
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    todos = db.relationship('Todo', backref='user', lazy=True)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(1000), nullable=False)
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/')
def index():
    todoList = Todo.query.order_by(Todo.id).all()
    return render_template('base.html', todo_list=todoList)

# add a task
@app.route('/add', methods=["POST"])
def add():
    
    # get the title of the task
    title = request.form.get("title")

    # if the title is empty then redirect to the index page
    if title == "":
        return redirect(url_for("index"))
    # create a todo object
    newTask = Todo(task=title, complete=False, user_id=1)  # Ajout d'un user_id par défaut
    
    # try to add the object to the database
    try:
        db.session.add(newTask)
        db.session.commit()
        return redirect(url_for("index"))
    except:
        return "There was an issue adding your task."


# delete a task
@app.route('/delete/<int:todo_id>')
def delete(todo_id):

    # get the task from the data base
    task = Todo.query.filter_by(id=todo_id).first()
    
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for("index"))
    except:
        return "There was an issue deleting your task."


# update a task
@app.route('/update/<int:todo_id>')
def update(todo_id):

    # get the task from the data base
    task = Todo.query.filter_by(id=todo_id).first()
    # toggle the complete value
    task.complete = not task.complete

    # try to commit to the database
    try:
        db.session.commit()
        return redirect(url_for("index"))
    except:
        return "There was an issue deleting your task."


if __name__ == "__main__":
    
    db.create_all()
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)
