from flask import Flask, redirect,render_template, request
import re
import os
import json
file_name = 'todo_list.json'
toDoList=[[]]
if os.path.exists(file_name):
    with open(file_name, 'r') as file:
        toDoList = json.load(file)
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_priority(priority):
    valid_priorities = ['Low', 'Medium', 'High']
    return priority in valid_priorities


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('todo_view.html', toDoList=toDoList)

@app.route('/submit', methods = ['POST'])
def submitForm():
    email = request.form['email']
    task = request.form['task']
    priority = request.form['priority']

    if validate_email(email) and validate_priority(priority):
        toDoList.append([task,email,priority])
    elif not(validate_email(email)):
         print(f"The email '{email}' is not valid.")

    elif not(validate_priority(priority)):
         print(f"The email '{priority}' is not valid.")     
    
    return redirect('/')

@app.route('/clear', methods = ['POST'])
def clearData():
   global toDoList
   toDoList = []
   return redirect('/')
@app.route('/save', methods=['POST'])
def save_list():
    global toDoList
    with open(file_name, 'w') as file:
        json.dump(toDoList, file)
    return redirect('/')


if __name__ == '__main__':
    app.run()


