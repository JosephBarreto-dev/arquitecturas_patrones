from flask import Flask, render_template, request, redirect
from models.task import TaskStore

app = Flask(__name__)
tasks = TaskStore()

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks.get_all())

@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form["title"]
        tasks.add(title)
        return redirect("/")
    return render_template("add_task.html")

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    tasks.complete(task_id)
    return redirect("/")
