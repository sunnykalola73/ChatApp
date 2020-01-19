from flask import Flask, request, render_template, make_response, session, redirect
import random
import time
import json
import sys
import sqlConnector
import hashlib
import threading
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'any random string'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error)

@app.route('/')
@app.route('/login')
def login():
    data = None
    username = request.cookies.get('username')
    data = {'username': username}
    return render_template('login.html', data=data)


@app.route('/logout')
def logout():
    data = None
    username = request.cookies.get('username')
    data = {'username': username}
    return render_template('logout.html', data=data)


@app.route('/signup')
def signup():
    data = None
    username = request.cookies.get('username')
    data = {'username': username}
    return render_template('signup.html', data=data)


@app.route('/chat')
def chat():
    data = None
    username = request.cookies.get('username')
    data = {'username': username}
    if username == None:
        return redirect('/login')
    person = request.cookies.get('person')
    if person == None:
        return redirect('/room')
    data.update({'person': person})

    def get_message(sender, receiver):
        data1 = sqlConnector.get_message(sender, receiver)
        data2 = sqlConnector.get_message(receiver, sender)
        # data1 = connection.Message.objects(username=username, person=person)
        # data2 = connection.Message.objects(username=person, person=username)
        print(data1)
        message = []
        for each in data1:
            message.append([each[0], each[1], True])
        for each in data2:
            message.append([each[0], each[1], False])
        message.sort(key=lambda x: x[1])
        return message
    data.update({'message': get_message(username, person)})
    return render_template('chat.html', data=data)


@app.route('/storemessage', methods=['POST'])
def store_message():
    username = request.cookies.get('username')
    person = request.cookies.get('person')
    if username == None:
        return redirect('/login')
    if person == None:
        return redirect('/room')
    try:
        message = request.form['message']
    except:
        return redirect('error.html')
    try:
        sqlConnector.save_message(
            senderMail=senderMail,
            receiverMail=receiverMail,
            message=message
        )
        # connection.Message(
        #     username=username,
        #     person=person,
        #     message=message,
        #     time=datetime.now()
        # ).save()
    except Exception as error:
        print(error)
    return ""


@app.route('/room')
def room():
    data = None
    username = request.cookies.get('username')
    data = {'username': username}
    if username == None:
        return redirect('/login')
    data.update({'users': get_user_list(username)})
    print(data)
    abc = session['username']
    return render_template('room.html', data=data, abc=abc)


def get_user_list(username):
    tmp = sqlConnector.get_users()
    user_list = []
    for i in tmp:
        if i != username:
            user_list.append(i)
    # for each in connection.User.objects:
    #     user_list.append(each.username)
    
    print(user_list)
    return user_list


def login_checker(password, email):
    print("Hello")
    res = sqlConnector.login_checker(password, email)
    print(res)
    if len(res) > 0:  # user exists
        # render_template('room.html',data=data)
        return True
    else:
        return False


def signup_checker(username, password, email):
    res = sqlConnector.signup_checker(username, password, email)
    print(res)
    return res


@app.route('/validator', methods=['POST', 'GET'])
def validator():
    
    try:
        try:
            if request.method == 'POST':
                source = request.form['page']
            elif request.method == 'GET':            
                source = request.args['page']
            password = request.form['password']
            email = request.form['email']
            print(source)
        except:
            return render_template('error.html', error="User can't request to this page directly.")
        if source == 'login':
            data = login_checker(password, email)
            # print(data)
        elif source == 'signup':
            username = request.form['username']
            data = signup_checker(username, password, email)
        else:
            return render_template('error.html', error="Invalid Request.")
    except:
        return render_template('error.html', error="Missing Fields.")
    if data == True:
        session['username'] = email
        data = session['username']
        return render_template('validator.html', data=data)
        #data = request.cookies.get("country")
        # return 'Welcome ' + data['username']
    else:
        return render_template('error.html', error=data)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Command usage: python app.py host port')
        exit(0)
    try:
        # connection.connect_to("chit-chat-room")
        #    -- Xampp  connection
        app.run(host=sys.argv[1], port=sys.argv[2], debug=True)
    except Exception as error:
        print(error)
