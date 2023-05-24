from flask import Flask, redirect, url_for, render_template, request
import mysql.connector

app = Flask(__name__)
port_number = 27205

def connect(command, values):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="P4ssw0rd",
        database="340_project"
    )
    mycursor = mydb.cursor()
    mycursor.execute(command, values)
    mydb.commit()

# index Page
@app.route("/")
def index():
    return render_template("index.html")

# venues Page
@app.route("/venues", methods=["GET", "POST"])
def venues():

    if request.method == "GET":
        pass

    if request.method == "POST":
        print(request.form)
        
        if request.form["method"] == "put":
            venue_id = int(request.form["venue_id"])
            address = request.form["address"]
            capacity = int(request.form["capacity"])
            email = request.form["email"]
            phone_number = request.form["phone_number"]

            command = "UPDATE Venues SET address = %s, capacity = %s, email = %s, phone_number = %s WHERE venue_id = %s;"
            values = (address, capacity, email, phone_number, venue_id)
            connect(command, values)

    return render_template("venues.html")

# artists Page
@app.route("/artists")
def artists():
    return render_template("artists.html")

# customers Page
@app.route("/customers")
def customers():
    return render_template("customers.html")

# concerts Page
@app.route("/concerts")
def concerts():
    return render_template("concerts.html")

# ticketsales Page
@app.route("/ticketsales")
def ticketsales():
    return render_template("ticketsales.html")

# intersection Page
@app.route("/concerts_ticketsales")
def concerts_ticketsales():
    return render_template("concerts_ticketsales.html")

if __name__ == "__main__":
    app.run(debug=True, port=port_number)
