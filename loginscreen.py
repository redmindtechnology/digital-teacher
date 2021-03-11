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
app.skl = ""
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
        app.skl = skl
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
        if role == "admin" and password == pwd and school == app.skl:
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
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s"
        val = (app.skl,)
        print(app.skl)
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

@app.route('/grade6', methods=['GET', 'POST'])
def grade6():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        mycursor = db_connection.cursor()

        print(app.skl)
        sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 6"
        val = (app.skl,)
        print(app.skl)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        #num_stud = len(myresult)
        num_stud = 0
        timeline = get_timeline()
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
        timeline = get_timeline()
        for x in myresult:
            # print(x)
            if x[4] > 0  and x[13] > timeline:
                num_chatbot_stud = num_chatbot_stud + 1

        activetrends.append({'Trend': 'Grade6 Total Students', 'Count': str(num_stud)})
        activetrends.append({'Trend': 'Grade6 Chatbot Students', 'Count': str(num_chatbot_stud)})
        mycursor.close()
        return jsonpify(json.dumps(activetrends))

    except:
        print("Error")

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
        timeline = get_timeline()
        for x in myresult:
            # print(x)
            if x[4] > 0 and x[13] > timeline:
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
        timeline = get_timeline()
        for x in myresult:
            # print(x)
            if x[4] > 0 and x[13] > timeline:
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
        timeline = get_timeline()
        for x in myresult:
            # print(x)
            if x[4] > 0 and x[13] > timeline:
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
        timeline = get_timeline()
        for x in myresult:
            # print(x)
            if x[4] > 0 and x[13] > timeline:
                num_chatbot_stud = num_chatbot_stud + 1

        print(num_chatbot_stud)

        activetrends.append({'Trend': 'Grade10 Total Students', 'Count': str(num_stud)})
        activetrends.append({'Trend': 'Grade10 Chatbot Students', 'Count': str(num_chatbot_stud)})
        mycursor.close()
        return jsonpify(json.dumps(activetrends))

    except:
        print("Error")


@app.route('/sub_wise', methods=['GET', 'POST'])
def sub_wise():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        # Get the students in Grade 6
        mycursor = db_connection.cursor()

        grade = [6, 7, 8, 9, 10]
        subject = ["English", "Civics", "History", "Geography", "Science"]
        activetrends = []
        timeline = get_timeline()
        for mygrade in grade:
            stud_count = [0, 0, 0, 0, 0]

            sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = %s"
            val = (app.skl, mygrade)
            # val = ("Holy Cross", mygrade)
            mycursor.execute(sql, val)
            myresult_1 = mycursor.fetchall()

            user_id = []
            for x in myresult_1:
                if x[13] > timeline:
                    user_id.append(x[0])
            print(user_id)

            for user in user_id:
                print(user)
                # Subject loop
                sub = 0
                for my_sub in subject:
                    sql_2 = "SELECT * from x8ur_chatbot_lesson_activity_tracker WHERE userid = %s AND subject = %s"
                    val_2 = (user, my_sub)
                    mycursor.execute(sql_2, val_2)
                    myresult_2 = mycursor.fetchall()
                    if len(myresult_2) > 0:
                        stud_count[sub] = stud_count[sub] + 1
                    sub = sub + 1

            activetrends.append({"sector": "English_Lesson", "size": stud_count[0]})
            activetrends.append({"sector": "English_Poem", "size": stud_count[0]})
            activetrends.append({"sector": "Civics", "size": stud_count[1]})
            activetrends.append({"sector": "History", "size": stud_count[2]})
            activetrends.append({"sector": "Geography", "size": stud_count[3]})
            activetrends.append({"sector": "Science", "size": stud_count[4]})

        mycursor.close()
        print(activetrends)

        # return activetrends
        return jsonpify(json.dumps(activetrends))

    except:
        print("Error")



# Get Trending Students
@app.route('/trends', methods=['GET', 'POST'])
def trends():
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                  connection_timeout=60000)
    mycursor = db_connection.cursor()
    activetrends = []
    sql = "SELECT * from x8ur_chatbot_user WHERE school = %s AND grade = 6"
    val = (app.skl,)
    print(app.skl)
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
    val = (app.skl,)
    print(app.skl)
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
    val = (app.skl,)
    print(app.skl)
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
    val = (app.skl,)
    print(app.skl)
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
    val = (app.skl,)
    print(app.skl)
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


@app.route('/topstudents', methods=['GET', 'POST'])
def topstudents():
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        # Get the students in Grade 6
        mycursor = db_connection.cursor()

        activetrends = []

        sql = "select firstname, loginattempt from x8ur_chatbot_user where school = %s order by loginattempt DESC limit 10"

        mycursor.execute(sql, (app.skl,))
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
    # check = sub_wise()
    app.run()
