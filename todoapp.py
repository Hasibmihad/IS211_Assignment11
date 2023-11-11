from flask import Flask, redirect,render_template, request
import re
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_priority(priority):
    valid_priorities = ['Low', 'Medium', 'High']
    return priority in valid_priorities


app = Flask(__name__)
toDoList=[['Buy Milk','123@gmail.com','High'],['Buy Cow','123cow@gmail.com','Medium']]
@app.route('/')
def hello_world():
    return redirect('/todo_view.html')



@app.route('/todo_view.html')
def view():
    return render_template('todo_view.html', toDoList=toDoList)

@app.route('/submit', methods = ['POST'])
def submit():
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



if __name__ == '__main__':
    app.run()

