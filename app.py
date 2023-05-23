from flask import Flask, redirect, url_for, render_template, request
import mysql.connector

app = Flask(__name__)
port_number = 27205

def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="340_project"
    )
    mycursor = mydb.cursor()
    return mycursor

# index Page
@app.route("/")
def index():
    return render_template("index.html")

# venues Page
@app.route("/venues", methods=["GET", "POST", "PUT", "DELETE"])
def venues():
    mycursor = connect()
    if request.method == "GET":
        pass

    if request.method == "POST":
        pass

    if request.method == "PUT":
        venue_id = request.form["venue_id"]
        address = request.form["address"]
        capacity = int(request.form["capacity"])
        email = request.form["email"]
        phone_number = request.form["phone_number"]

        command = "UPDATE Venues SET address = %s, capacity = %d, email = %s, phone_number = %s \
            WHERE venue_id = %d;"
        mycursor.execute(command, (address, capacity, email, phone_number, venue_id))

    if request.method == "DELETE":
        pass

    return render_template("venues.html")

# venues Page
@app.route("/artists")
def artists():
    return render_template("artists.html")

# venues Page
@app.route("/customers")
def customers():
    return render_template("customers.html")

# venues Page
@app.route("/concerts")
def concerts():
    return render_template("concerts.html")

# venues Page
@app.route("/ticketsales")
def ticketsales():
    return render_template("ticketsales.html")

# venues Page
@app.route("/concerts_ticketsales")
def concerts_ticketsales():
    return render_template("concerts_ticketsales.html")

if __name__ == "__main__":
    app.run(debug=True, port=port_number)
