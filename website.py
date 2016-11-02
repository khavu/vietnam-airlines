import pymysql
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flaskext.mysql import MySQL

# create our little application
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123.abc'
app.config['MYSQL_DATABASE_DB'] = 'vnairline'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


def connect_db():
    database = mysql.connect()
    cursor = database.cursor()
    return cursor


@app.route("/")
def home():
    return "Welcome to my website"


@app.route("/search", methods=['POST'])
def search():
    request.form['inputSearch']


@app.route("/projects/vnairline")
def show_user_info():
    fields = "ID_NUMBER,EMBOSSED_NAME,DOB1,GENDER,CREATE_DATE,STATUS_CODE,SALUTATION,BUS_COMPANY_NAME," \
             "STREET_FREE_TEXT,ADDRESS_2,ADDRESS_3,CITY_NAME,STATE_PROVINCE_NAME," \
             "POSTAL_CODE,COUNTRY,EMAIL_ADDRESS"

    cur = connect_db()
    cur.execute("select %s from vnairline.user_info limit 1000;" % fields)
    user_info = cur.fetchall()
    print(user_info)
    return render_template('vnairline.html', fields=fields.split(','), user_info=user_info)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)

