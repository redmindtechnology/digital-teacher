import mysql.connector
import mysql.connector as mysql
import json
import time
import datetime
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

now = datetime.datetime.now()
dt_string = now.strftime('%Y/%m/%d %H:%M:%S')
#app.skl = ""
app.interval = "Weekly"


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
        # sql = "SELECT  pwd FROM user WHERE email="+username
        sql = "SELECT * FROM x8ur_chatbot_user WHERE username = %s"
        val = (username,)
        # val=str(username)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        role = ""
        school = ""
        for x in myresult:
            # print(x)
            role = x[11]
            password = x[3]
            school = x[8]
            # print(role)
        mycursor.close()
        if role == "admin" and password == pwd and school == skl:
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

@app.route('/get_interval', methods=['GET', 'POST'])
def get_interval():
    try:
        app.interval = request.args.get('interval')
        print(app.interval)
        return jsonpify("OK")
    except:
        print("Error in get_interval")

def get_timeline():
    current = datetime.datetime.now()
    print(current)
    if app.interval == "Weekly":
        timeline = current - datetime.timedelta(days=7)
    if app.interval == "Monthly":
        timeline = current - datetime.timedelta(days=30)
    if app.interval == "Yearly":
        timeline = current - datetime.timedelta(days=365)
    if app.interval == "Today":
        timeline = current.replace(hour=0, minute=0, second=0, microsecond=0)
    return timeline



@app.route('/overallgrade', methods=['GET', 'POST'])
def overallgrade():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        schoolname = str(request.args.get('skl'))
        print(schoolname)
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s"
        val = (schoolname,)
        print(schoolname)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        num_stud = len(myresult)
        num_stud = 0
        timeline = get_timeline()
        for x in myresult:
            if x[13] > timeline:
                num_stud = num_stud + 1

        print(num_stud)
        mycursor.close()
        return jsonpify(num_stud)


    except:
        print("Error")
        # print("Error Code:", err.errno)
        # print("SQLSTATE", err.sqlstate)
        # print("Message", err.msg)
        # return jsonpify(err)

@app.route('/grade', methods=['GET', 'POST'])
def grade():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        stud_grade = request.args.get('grade')
        schoolname = request.args.get('skl')
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = %s"
        val = (schoolname, stud_grade)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        #num_stud = len(myresult)
        num_stud = 0
        timeline = get_timeline()
        print(timeline)
        for x in myresult:
            if x[13] > timeline:
                num_stud = num_stud + 1

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
    activetrends = []
    schoolname = request.args.get('skl')
    sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 6"
    val = (schoolname,)
    print(schoolname)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    num_stud = len(myresult)
    print(num_stud)
    num_chatbot_stud = 0
    timeline = get_timeline()
    for x in myresult:
        # print(x)
        if x[4] > 0 and x[13] > timeline:
            num_chatbot_stud = num_chatbot_stud + 1

    activetrends.append({'Trend': 'Grade6 Total Students', 'Count': str(num_stud)})
    activetrends.append({'Trend': 'Grade6 Chatbot Students', 'Count': str(num_chatbot_stud)})
    sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 7"
    val = (schoolname,)
    print(schoolname)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    num_stud = len(myresult)
    print(num_stud)
    num_chatbot_stud = 0
    for x in myresult:
        # print(x)
        if x[4] > 0  and x[13] > timeline:
            num_chatbot_stud = num_chatbot_stud + 1

    activetrends.append({'Trend': 'Grade7 Total Students', 'Count': str(num_stud)})
    activetrends.append({'Trend': 'Grade7 Chatbot Students', 'Count': str(num_chatbot_stud)})
    sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 8"
    val = (schoolname,)
    print(schoolname)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    num_stud = len(myresult)
    print(num_stud)
    num_chatbot_stud = 0
    for x in myresult:
        # print(x)
        if x[4] > 0 and x[13] > timeline:
            num_chatbot_stud = num_chatbot_stud + 1

    activetrends.append({'Trend': 'Grade8 Total Students', 'Count': str(num_stud)})
    activetrends.append({'Trend': 'Grade8 Chatbot Students', 'Count': str(num_chatbot_stud)})
    sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 9"
    val = (schoolname,)
    print(schoolname)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    num_stud = len(myresult)
    print(num_stud)
    num_chatbot_stud = 0
    for x in myresult:
        # print(x)
        if x[4] > 0 and x[13] > timeline:
            num_chatbot_stud = num_chatbot_stud + 1

    activetrends.append({'Trend': 'Grade9 Total Students', 'Count': str(num_stud)})
    activetrends.append({'Trend': 'Grade9 Chatbot Students', 'Count': str(num_chatbot_stud)})
    sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 10"
    val = (schoolname,)
    print(schoolname)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    num_stud = len(myresult)
    print(num_stud)
    num_chatbot_stud = 0
    for x in myresult:
        # print(x)
        if x[4] > 0 and x[13] > timeline:
            num_chatbot_stud = num_chatbot_stud + 1

    activetrends.append({'Trend': 'Grade10 Total Students', 'Count': str(num_stud)})
    activetrends.append({'Trend': 'Grade10 Chatbot Students', 'Count': str(num_chatbot_stud)})
    mycursor.close()
    return jsonpify(json.dumps(activetrends))

@app.route('/get_top6_quiz', methods=['GET', 'POST'])
def get_top6_quiz():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()
        sql = "SELECT * from x8ur_chatbot_quiz_activity_tracker"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        quiz_scores = {}
        for x in myresult:
            if x[1] in quiz_scores:
                quiz_scores[x[1]] = quiz_scores[x[1]] + x[4]
            else:
                quiz_scores[x[1]] = x[4]

        print(quiz_scores)
        sorted_quiz_scores = dict(sorted(quiz_scores.items(), key=lambda item: item[1], reverse=True))
        print(sorted_quiz_scores)

        activetrends = []

        for user_id in sorted_quiz_scores:
            print(user_id)
            sql = "SELECT firstname from x8ur_chatbot_user where id=%s"
            val = (user_id,)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchone()
            activetrends.append({'country': str(myresult[0]), 'visits': str(sorted_quiz_scores[user_id])})
            print(str(myresult))

        mycursor.close()
        return jsonpify(json.dumps(activetrends))

    except:
        print("Error")

@app.route('/topstudents', methods=['GET', 'POST'])
def topstudents():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        # Get the students in Grade 6
        mycursor = db_connection.cursor()
        schoolname = request.args.get('skl')
        activetrends = []

        sql = "select firstname, loginattempt from x8ur_chatbot_user where school = %s order by loginattempt DESC limit 10"

        val = (schoolname, )
        mycursor.execute(sql, val)
        myresult_all = mycursor.fetchall()

        for row in myresult_all:
            activetrends.append({'Name': row[0], 'no of login': str(row[1])})

        mycursor.close()
        print(activetrends)

        # return activetrends
        return jsonpify(json.dumps(activetrends))

    except:
        print("Error")

if __name__ == '__main__':
    app.run()

