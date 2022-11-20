from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)

@app.route('/')
def all_user():
    users = User.get_all()
    return render_template('read.html', users = users)

@app.route('/new_user')
def new_user():
    return render_template('create.html')

@app.route('/create_user', methods = ['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.create_user(data)
    return redirect('/show_last_user')

@app.route('/show_last_user')
def show_last_user():
    result = User.get_all()
    the_user = result[-1]
    return render_template('users_read.html', the_user = the_user)

@app.route('/show_user/<int:id>')
def show_user(id):
    result = User.get_all()
    for user in result:
        if user.id == id:
            the_user = user
    return render_template('users_read.html', the_user = the_user)

@app.route('/edit/<int:id>')
def edit_user(id):
    result = User.get_all()
    for user in result:
        if user.id == id:
            the_user = user
    return render_template('edit.html', the_user = the_user)

@app.route('/delete/<int:id>')
def delete_user(id):
    data={
        'id': id
    }
    User.delete_user(data)
    return redirect('/')

@app.route('/update/<int:id>', methods = ['POST'])
def update_user(id):
    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)