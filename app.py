from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
# # это походу коментарий 
# @app.route("/")
# def index():
#     return render_template ("base.html") 

# То что было будем комментировать, а то что новое будет нагромаждатся сдальше
# тем болле что я выучтл комментарии, все прихордит во время практики
# чтобы кодить нужно кодить - вот простая истинна которую нужно помнить.

# @app.route("/add", methods=["POST"])
# def add():
#     task = request.form.get("new_task")
#     print(f"Получена задача: {task}")
#     return redirect("/")

# Потом мы уже не просто будем отображать base.html
# но и подтягивать на главную страницу бд. Корневую функция на сторках 6-8
# перепишем 
@app.route("/")
def index():
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    cursor.execute("SELECT id, content FROM tasks")
    tasks = cursor.fetchall()
    connection.close()
    return render_template("base.html", task=tasks)


@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("new_task")
    # подключаемся к базе данных
    connection = sqlite3.connect("db.sqlite3")
    # затем ставим курсор для того чтобы начать писать запросы в БД
    cursor = connection.cursor()
    # и  затем вставлем в поле те данне которые мы получим от пользователя
    cursor.execute("INSERT INTO tasks (content) VALUES (?)", (task,))
    connection.commit()
    connection.close()
    print(f"Получена задача: {task}")
    return redirect("/")

# В задании T7 - я так пониаю мы будем писать фенкцию на удаление строки из БД
@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")
    


if __name__ == "__main__":
    app.run(debug=True, port=8000)

