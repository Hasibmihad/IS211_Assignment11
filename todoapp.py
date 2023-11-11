from flask import Flask, redirect,render_template
app = Flask(__name__)

toDoList=[['Buy Milk','123@gmail.com','High'],['Buy Cow','123cow@gmail.com','Medium']]
@app.route('/')
def hello_world():
    return redirect('/todo_view.html')



@app.route('/todo_view.html')
def view():
    return render_template('todo_view.html', toDoList=toDoList)





if __name__ == '__main__':
    app.run()

