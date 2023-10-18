from flask import Flask, request, render_template, redirect, url_for
import openpyxl
from openpyxl import Workbook
from datetime import datetime

def add_link(link, ip, user):
    try:
        workbook = openpyxl.load_workbook("./exel/links.xlsx")
    except FileNotFoundError:
        workbook = Workbook()
        workbook.active.append(['User', 'Link', 'Date', 'IP'])
    sheet = workbook.active

    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    sheet.append([user, link, current_datetime, ip])

    workbook.save("./exel/links.xlsx")

def check_login(username, password):
    workbook = openpyxl.load_workbook('./exel/goscie.xlsx')
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0] == username and row[1] == password:
            return True

    return False

app = Flask(__name__, template_folder='templates')

@app.route('/')
def init():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']        
        
        if check_login(username, password):
            return redirect(url_for('sending', user=username))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route("/send/<user>", methods=["GET", "POST"])
def sending(user):
    if request.method == "POST":
        link = request.form.get("link")
        ip_adress = request.remote_addr

        add_link(link, ip_adress, user)

    return render_template("send.html")