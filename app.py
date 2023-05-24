from flask import Flask, redirect, url_for, render_template, request
import mysql.connector

app = Flask(__name__)
port_number = 27205

def connect(command, values=None):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="P4ssw0rd",
        database="340_project"
    )
    mycursor = mydb.cursor()
    if values:
        mycursor.execute(command, values)
        mydb.commit()
    else:
        mycursor.execute(command)

    if 'SELECT' in command:
        return mycursor.fetchall()

# index Page
@app.route("/")
def index():
    return render_template("index.html")

# venues Page
@app.route("/venues", methods=["GET", "POST"])
def venues():
    # READ
    if request.method == 'GET':
        # SQL select Venues table data
        query = 'SELECT * FROM Venues;'
        venue_data = connect(query)
        print(venue_data)
        # render table through .j2 file
        return render_template('venues.html', venues=venue_data)

    # CREATE
    elif request.method == 'POST':
         # user clicks 'new'
        if request.form.get('insert_venue'):
            address = request.form['address']
            capacity = request.form['capacity']
            email = request.form['email']
            phone_number = request.form['phone_number']
            # insert new row into Venues
            query = 'INSERT INTO Venues (address, capacity, email, phone_number) VALUES (%s, %s, %s, %s);'
            values = (address, capacity, email, phone_number)
            connect(query, values)
            # redirect to /venues
            return redirect("/venues")
        
        if request.form["method"] == "put":
            venue_id = int(request.form["venue_id"])
            address = request.form["address"]
            capacity = int(request.form["capacity"])
            email = request.form["email"]
            phone_number = request.form["phone_number"]

            command = "UPDATE Venues SET address = %s, capacity = %s, email = %s, phone_number = %s WHERE venue_id = %s;"
            values = (address, capacity, email, phone_number, venue_id)
            connect(command, values)
            return redirect("/venues")
        
        if request.form["method"] == "delete":
            venue_id = int(request.form["venue_id"])

            command = "DELETE FROM Venues WHERE venue_id = %s"
            values = (venue_id,)
            connect(command, values)
            return redirect("/venues")

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
