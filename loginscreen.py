import mysql.connector
import mysql.connector as mysql
import json
import time
from datetime import datetime
from time import sleep
import os
import sys
from json import loads
from flask import Flask, render_template, session
from flask import request, render_template
import re
# from flask import send_from_directory, url_for
from flask_jsonpify import jsonpify

app = Flask(__name__)

# enter your server IP address/domain name
HOST = "redmindtechnologies.com"  # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "u852023448_uwyeF"
# this is the user you create
USER = "u852023448_MfN4p"
# user password
PASSWORD = "xR1smqFRrV"

now = datetime.now()
dt_string = now.strftime('%Y/%m/%d %H:%M:%S')
app.skl = ""

# Login Page Validation
@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        username = request.args.get('username')
        username = re.sub("'", "", username)
        pwd = (request.args.get('password'))
        skl = (request.args.get('skl'))
        print(username)
        print(pwd)
        print(skl)
        app.skl = skl
        # sql = "SELECT  pwd FROM user WHERE email="+username
        sql = "SELECT * FROM x8ur_chatbot_user WHERE username = %s"
        val = (username,)
        # val=str(username)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        role = ""
        for x in myresult:
            #print(x)
            role = x[11]
            password = x[3]
            #print(role)
        mycursor.close()
        if role == "admin" and password == pwd:
            print("Correct Password")
            return jsonpify("OK")
        else:
            print("Incorrect Password")
            return jsonpify("Error")

    except:
        print("Error")
        # print("Error Code:", err.errno)
        # print("SQLSTATE", err.sqlstate)
        # print("Message", err.msg)
        # return jsonpify(err)

@app.route('/grade6', methods=['GET', 'POST'])
def grade6():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 6"
        val = (app.skl,)
        print(app.skl)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        num_stud = len(myresult)
        print(num_stud)
        mycursor.close()
        return jsonpify(num_stud)


    except:
        print("Error")
        # print("Error Code:", err.errno)
        # print("SQLSTATE", err.sqlstate)
        # print("Message", err.msg)
        # return jsonpify(err)

@app.route('/grade7', methods=['GET', 'POST'])
def grade7():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 7"
        val = (app.skl,)
        print(app.skl)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        num_stud = len(myresult)
        print(num_stud)
        mycursor.close()
        return jsonpify(num_stud)


    except:
        print("Error")
        # print("Error Code:", err.errno)
        # print("SQLSTATE", err.sqlstate)
        # print("Message", err.msg)
        # return jsonpify(err)


@app.route('/grade7a', methods=['GET', 'POST'])
def grade7a():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 7"
        val = (app.skl,)
        print(app.skl)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        num_stud = len(myresult)
        print(num_stud)
        num_chatbot_stud = 0
        activetrends = []

        for x in myresult:
            # print(x)
            if x[4] > 0:
                num_chatbot_stud = num_chatbot_stud + 1

        activetrends.append({'Trend': 'Grade7 Total Students', 'Count': str(num_stud)})
        activetrends.append({'Trend': 'Grade7 Chatbot Students', 'Count': str(num_chatbot_stud)})
        mycursor.close()
        return jsonpify(json.dumps(activetrends))

    except:
     print("Error")


# print("Error Code:", err.errno)
# print("SQLSTATE", err.sqlstate)
# print("Message", err.msg)
# return jsonpify(err)

@app.route('/grade6a', methods=['GET', 'POST'])
def grade6a():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 6"
        val = (app.skl,)
        print(app.skl)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        num_stud = len(myresult)
        print(num_stud)
        num_chatbot_stud = 0
        activetrends = []

        for x in myresult:
            # print(x)
            if x[4] > 0:
                num_chatbot_stud = num_chatbot_stud + 1

        activetrends.append({'Trend': 'Grade6 Total Students', 'Count': str(num_stud)})
        activetrends.append({'Trend': 'Grade6 Chatbot Students', 'Count': str(num_chatbot_stud)})
        mycursor.close()
        return jsonpify(json.dumps(activetrends))

    except:
     print("Error")

@app.route('/grade8a', methods=['GET', 'POST'])
def grade8a():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 8"
        val = (app.skl,)
        print(app.skl)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        num_stud = len(myresult)
        print(num_stud)
        num_chatbot_stud = 0
        activetrends = []

        for x in myresult:
            # print(x)
            if x[4] > 0:
                num_chatbot_stud = num_chatbot_stud + 1

        activetrends.append({'Trend': 'Grade8 Total Students', 'Count': str(num_stud)})
        activetrends.append({'Trend': 'Grade8 Chatbot Students', 'Count': str(num_chatbot_stud)})
        mycursor.close()
        return jsonpify(json.dumps(activetrends))

    except:
     print("Error")

@app.route('/grade9a', methods=['GET', 'POST'])
def grade9a():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 9"
        val = (app.skl,)
        print(app.skl)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        num_stud = len(myresult)
        print(num_stud)
        num_chatbot_stud = 0
        activetrends = []

        for x in myresult:
            # print(x)
            if x[4] > 0:
                num_chatbot_stud = num_chatbot_stud + 1

        activetrends.append({'Trend': 'Grade9 Total Students', 'Count': str(num_stud)})
        activetrends.append({'Trend': 'Grade9 Chatbot Students', 'Count': str(num_chatbot_stud)})
        mycursor.close()
        return jsonpify(json.dumps(activetrends))

    except:
     print("Error")

@app.route('/grade10a', methods=['GET', 'POST'])
def grade10a():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 10"
        val = (app.skl,)
        print(app.skl)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        num_stud = len(myresult)
        print(num_stud)
        num_chatbot_stud = 0
        activetrends = []

        for x in myresult:
            # print(x)
            if x[4] > 0:
                num_chatbot_stud = num_chatbot_stud + 1

        activetrends.append({'Trend': 'Grade10 Total Students', 'Count': str(num_stud)})
        activetrends.append({'Trend': 'Grade10 Chatbot Students', 'Count': str(num_chatbot_stud)})
        mycursor.close()
        return jsonpify(json.dumps(activetrends))

    except:
     print("Error")

@app.route('/grade8', methods=['GET', 'POST'])
def grade8():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 8"
        val = (app.skl,)
        print(app.skl)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        num_stud = len(myresult)
        print(num_stud)
        mycursor.close()
        return jsonpify(num_stud)


    except:
        print("Error")
        # print("Error Code:", err.errno)
        # print("SQLSTATE", err.sqlstate)
        # print("Message", err.msg)
        # return jsonpify(err)

@app.route('/grade9', methods=['GET', 'POST'])
def grade9():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 9"
        val = (app.skl,)
        print(app.skl)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        num_stud = len(myresult)
        print(num_stud)
        mycursor.close()
        return jsonpify(num_stud)


    except:
        print("Error")
        # print("Error Code:", err.errno)
        # print("SQLSTATE", err.sqlstate)
        # print("Message", err.msg)
        # return jsonpify(err)

@app.route('/grade10', methods=['GET', 'POST'])
def grade10():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 10"
        val = (app.skl,)
        print(app.skl)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        num_stud = len(myresult)
        print(num_stud)
        mycursor.close()
        return jsonpify(num_stud)


    except:
        print("Error")
        # print("Error Code:", err.errno)
        # print("SQLSTATE", err.sqlstate)
        # print("Message", err.msg)
        # return jsonpify(err)

# Get Trending Students
@app.route('/trends', methods=['GET', 'POST'])
def trends():
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                  connection_timeout=60000)
    mycursor = db_connection.cursor()
    activetrends=[]
    sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 6"
    val = (app.skl,)
    print(app.skl)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    num_stud = len(myresult)
    print(num_stud)
    num_chatbot_stud = 0
    for x in myresult:
        # print(x)
        if x[4] > 0:
            num_chatbot_stud = num_chatbot_stud + 1

    activetrends.append({'Trend':'Grade6 Total Students','Count':str(num_stud)})
    activetrends.append({'Trend':'Grade6 Chatbot Students','Count':str(num_chatbot_stud)})
    sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 7"
    val = (app.skl,)
    print(app.skl)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    num_stud = len(myresult)
    print(num_stud)
    num_chatbot_stud = 0
    for x in myresult:
        # print(x)
        if x[4] > 0:
            num_chatbot_stud = num_chatbot_stud + 1

    activetrends.append({'Trend': 'Grade7 Total Students', 'Count': str(num_stud)})
    activetrends.append({'Trend': 'Grade7 Chatbot Students', 'Count': str(num_chatbot_stud)})
    sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 8"
    val = (app.skl,)
    print(app.skl)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    num_stud = len(myresult)
    print(num_stud)
    num_chatbot_stud = 0
    for x in myresult:
        # print(x)
        if x[4] > 0:
            num_chatbot_stud = num_chatbot_stud + 1

    activetrends.append({'Trend': 'Grade8 Total Students', 'Count': str(num_stud)})
    activetrends.append({'Trend': 'Grade8 Chatbot Students', 'Count': str(num_chatbot_stud)})
    sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 9"
    val = (app.skl,)
    print(app.skl)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    num_stud = len(myresult)
    print(num_stud)
    num_chatbot_stud = 0
    for x in myresult:
        # print(x)
        if x[4] > 0:
            num_chatbot_stud = num_chatbot_stud + 1

    activetrends.append({'Trend': 'Grade9 Total Students', 'Count': str(num_stud)})
    activetrends.append({'Trend': 'Grade9 Chatbot Students', 'Count': str(num_chatbot_stud)})
    sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 10"
    val = (app.skl,)
    print(app.skl)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    num_stud = len(myresult)
    print(num_stud)
    num_chatbot_stud = 0
    for x in myresult:
        # print(x)
        if x[4] > 0:
            num_chatbot_stud = num_chatbot_stud + 1

    activetrends.append({'Trend': 'Grade10 Total Students', 'Count': str(num_stud)})
    activetrends.append({'Trend': 'Grade10 Chatbot Students', 'Count': str(num_chatbot_stud)})
    mycursor.close()
    return jsonpify(json.dumps(activetrends))

# Logout
# @app.route('/logout')
# def logout():
#	if 'username' in session:
#		session.pop('username', None)
#	return jsonpify({'message' : 'You successfully logged out'})

# @app.route('/getActiveRobots', methods=['GET', 'POST'])
# def getActiveRobots():
#    try:
#       db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,connection_timeout=60000)
#       #print("Connected to:", db_connection.get_server_info())
#      mycursor = db_connection.cursor()
#      tr="""select user from x8ur_chatbot_user where role='admin' """;
#     mycursor.execute(tr)
#    count=mycursor.fetchall()
#   #print (username)
#   results=jsonpify(count)
# print(results)
#  return results

# except mysql.Error as err:
#    return jsonpify("ok")

if __name__ == '__main__':
    app.run()
