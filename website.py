
import string
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


def search_entry(inputsearch, inputsearch_birthday, page):
    if whitelist(inputsearch) and whitelist(inputsearch_birthday):
        cur = connect_db()
        cur.execute("select {fields} from vnairline.user_info where EMBOSSED_NAME like '%%{inputsearch}%%' "
                    "and DOB1 like '%%{inputsearch_birthday}%%'"
                    "limit {page},25;".
                    format(fields=fields, inputsearch=inputsearch, inputsearch_birthday=inputsearch_birthday,
                           page=25 * (page - 1)))
        outputsearch = cur.fetchall()
        cur.execute("select count(*) from vnairline.user_info where EMBOSSED_NAME like '%%{inputsearch}%%'"
                    "and DOB1 like '%%{inputsearch_birthday}%%';".
                    format(fields=fields, inputsearch=inputsearch, inputsearch_birthday=inputsearch_birthday))
        count_search = cur.fetchall()
        last_page = int(list(count_search)[0][0] / 25) + 1
        return outputsearch, last_page
    else:
        return "error_inputsearch", "1"


def whitelist(textinput):
    white_list = list(string.ascii_letters + string.digits + string.whitespace + "/")
    for char in list(textinput):
        if white_list.count(char) > 0:
            pass
        else:
            return False
    return True


@app.route("/")
def home():
    return "Welcome to my website"


@app.route("/projects/vnairline", methods=['GET', 'POST'])
def show_user_info():
    if not request.args.get('page'):
        page = 1
    else:
        page = int(request.args.get('page'))

    if request.method == 'POST':
        if not request.form['inputsearch'] and not request.form['inputsearch_birthday']:
            session.clear()
            contents = None
            last_page = None
        else:
            session['inputsearch'] = request.form['inputsearch']
            session['inputsearch_birthday'] = request.form['inputsearch_birthday']
            contents, last_page = search_entry(session['inputsearch'], session['inputsearch_birthday'], page)
    else:
        if session and (session['inputsearch'] or session['inputsearch_birthday']):
            contents, last_page = search_entry(session['inputsearch'], session['inputsearch_birthday'], page)
        else:
            contents = None
            last_page = None

    print(session)
    
    if contents is None or last_page is None:
        cur = connect_db()
        cur.execute("select %s from vnairline.user_info limit %d,25;" % (fields, 25 * (page - 1)))
        user_info = cur.fetchall()
        last_page = 16402
    else:
        user_info = contents
        last_page = last_page

    return render_template('vnairline.html', fields=fields.split(','), user_info=user_info, page=page,
                           last_page=last_page)


if __name__ == "__main__":
    app.secret_key = 'vqk12#$56'

    fields = "EMBOSSED_NAME,DOB1,GENDER,CREATE_DATE,STATUS_CODE,SALUTATION,BUS_COMPANY_NAME," \
             "STREET_FREE_TEXT,ADDRESS_2,ADDRESS_3,CITY_NAME,STATE_PROVINCE_NAME," \
             "POSTAL_CODE,POINTS_EXP_DATE,POINTS_EXP_AMOUNT,COUNTRY,EMAIL_ADDRESS"

    app.run('0.0.0.0', 5000)
