from datetime import datetime
from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    SNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.SNo} - {self.title}"

@app.route("/", methods=["GET", "POST"])
def hello_world():

    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]

        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodos = Todo.query.all()

    return render_template("index.html", allTodos=allTodos)


if __name__ == "__main__":
    app.run(debug=True, port=8000)