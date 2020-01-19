import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="users"
)
mycursor = mydb.cursor()


def get_message(sender, receiver):
    sql = "select message,time from messages where senderMail='" + \
        sender+"' AND  receiverMail='"+receiver+"'"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data
    # data = mycursor.execute("show databases")
    # for i in data:
    #     print(i[1],type(i[1]))


def save_message(senderMail, receiverMail, message):
    print("here")
    sql = "insert into messages (senderMail, receiverMail, message) VALUES (%s, %s, %s)"
    val = (senderMail, receiverMail, message)
    mycursor.execute(sql, val)
    mydb.commit()


def get_username(name):
    print(name)
    sql = "select username from userinfo where email='"+name+"'"
    mycursor.execute(sql)
    data = str(mycursor.fetchall())
    data = data.split("'")[1]
    return data


def get_user_email():
    sql = "select email from userinfo"
    mycursor.execute(sql)
    return_data = []
    data = mycursor.fetchall()
    for each in data:
        each = str(each).split("'")[1]
        return_data.append(each)
    return return_data


def get_users():
    sql = "select username,email from userinfo"
    mycursor.execute(sql)
    tmp = mycursor.fetchall()
    return tmp


def login_checker(password, email):
    sql = "select username from userinfo where password=%s AND email=%s"
    val = (password, email)
    mycursor.execute(sql, val)
    data = mycursor.fetchall()
    return data


def signup_checker(username, password, email):
    try:
        sql = "insert into userinfo (username, password, email) values (%s, %s, %s)"
        val = (username, password, email)
        data = mycursor.execute(sql, val)
        data1 = mydb.commit()
        return True
    except Exception:
        return False
# get_message('sunnykalola73@gmail.com', 'rajkarkar007@gmail.com')

# get_message('rajkarkar007@gmail.com', 'sunnykalola73@gmail.com')
