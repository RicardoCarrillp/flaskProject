from flask import Flask, jsonify, render_template, url_for, redirect, request
from users import User
from flask_modus import Modus

app = Flask(__name__)
userss = []
modus = Modus(app)


def find_user(Uid):
    return [user for user in userss if user.id == Uid][0]


@app.route('/')
def root():
    return redirect(url_for('users'))


@app.route('/users', methods=['GET', 'POST', 'PATCH'])
def users():

    return render_template('index.html', users=userss)

@app.route('/users/new', methods=['GET', 'POST', 'PATCH'])
def new():
    if request.method == 'POST':
        new_user = User(
            request.form['first_name'],
            request.form['last_name'],
            request.form['phone'])

        userss.append(new_user)
        return redirect(url_for('users'))

    return render_template('new.html')


@app.route('/users/<int:id>', methods=["GET", "PATCH"])
def edit(id):
    userID = find_user(id)
    print(request.method)
    if request.method == b'PATCH':
        userID.first_name = request.form['first_name']
        userID.last_name = request.form['last_name']
        userID.phone = request.form['phone']
        return redirect(url_for('users'))

    return render_template('edit.html', user=userID)


@app.route('/users/delete/<int:id>', methods=["GET", "DELETE"])
def delete(id):
    userID = find_user(id)
    if request.method == b'DELETE':
        userss.remove(userID)
        return redirect((url_for('users')))

    return render_template('delete.html', user=userID)


if __name__ == '__main__':
    app.run()
