from flask import Flask, request, render_template
import openpyxl
from openpyxl import Workbook
from datetime import datetime

def add_link(link, ip):
    try:
        workbook = openpyxl.load_workbook("./exel/links.xlsx")
    except FileNotFoundError:
        workbook = Workbook()
        workbook.active.append(['Link', 'Data', 'IP'])
    sheet = workbook.active

    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    sheet.append([link, current_datetime, ip])

    workbook.save("./exel/links.xlsx")

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form.get("link")
        ip_adress = request.remote_addr

        add_link(link, ip_adress)

    return render_template("index.html")
