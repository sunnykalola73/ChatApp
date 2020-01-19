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
    try:
        username = session['username']
        data = {'username': username}
        return redirect('/room')
        # return render_template('login.html', data=data)
    except:
        data = None
        data = {'username': None}
        return render_template('login.html', data=data)


@app.route('/logout')
def logout():
    data = None
    username = session.pop('username')
    data = {'username': username}
    return render_template('logout.html', data=data)


@app.route('/signup')
def signup():
    try:
        data = None
        username = session['username']
        data = {'username': username}
        return redirect('/room')
        # return render_template('signup.html', data=data)
    except:
        data = None
        data = {'username': None}
        return render_template('signup.html', data=data)


@app.route('/chat')
def chat():
    data = None
    try:
        tmp = session['username']
        username = sqlConnector.get_username(tmp)
        
        if username == None:
            return redirect('/login')
        data = {'senderMail': username}
        try:
            receiverMail = request.cookies.get('receiverMail')
            data.update({'receiverMail': receiverMail})
            
            if receiverMail == None:
                return redirect('/room')
            else:
                
                data['message'] = get_message(tmp, receiverMail)
                data['receiverName'] = sqlConnector.get_username(receiverMail)
                return render_template('chat.html', data=data)
        except:
            print("2")
            return redirect('/room')
    except:
        return redirect('/login')

@app.route('/getmessage', methods=['POST'])
def getmessage():
    sender = session['username']
    receiver = request.form['receiverMail']
    x=get_message(sender,receiver)
    print(sender,receiver,x)
    return {'message':x}

def get_message(sender, receiver):
    data1 = sqlConnector.get_message(sender, receiver)
    data2 = sqlConnector.get_message(receiver, sender)
    # data1 = connection.Message.objects(username=username, person=person)
    # data2 = connection.Message.objects(username=person, person=username)
    # print(data1)
    message = []
    for each in data1:
        message.append([each[0], each[1], True])
    for each in data2:
        message.append([each[0], each[1], False])
    message.sort(key=lambda x: x[1])
    return message
# data.update({'message': get_message(username, person)})


@app.route('/storemessage', methods=['POST'])
def store_message():
    print("Abcdefghijklm")
    senderMail = session['username']
    receiverMail = request.cookies.get('receiverMail')
    if senderMail == None:
        return redirect('/login')
    if receiverMail == None:
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
    username = session['username']
    data = {'username': username}
    if username == None:
        return redirect('/login')
    abc = session['username']
    tmp_data = get_user_list(abc)
    print(tmp_data)
    data.update({'users': tmp_data[0]})
    data.update({'email': tmp_data[1]})
    return render_template('room.html', data=data, abc=abc)


def get_user_list(username):
    tmp = sqlConnector.get_users()
    user_list = [[], []]
    for i in tmp:
        if username != i[1]:
            user_list[0].append(i[0])
            user_list[1].append(i[1])
    return user_list


def login_checker(password, email):
    res = sqlConnector.login_checker(password, email)
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
    elif source == 'signup':
        return render_template('error.html', error="User already exist..")
    else:
        return render_template('error.html', error="Incorrect Credentials..!")


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
