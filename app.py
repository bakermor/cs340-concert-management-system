from flask import Flask, redirect, url_for, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
port_number = 25693

app.config['MYSQL_HOST'] = "classmysql.engr.oregonstate.edu"
app.config['MYSQL_USER'] = "cs340_bakermor"
app.config['MYSQL_PASSWORD'] = "0384"
app.config['MYSQL_DB'] = "cs340_bakermor"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

def connect(command, values=None):
    
    mycursor = mysql.connection.cursor()
    if values:
        mycursor.execute(command, values)
        mysql.connection.commit()
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
        # render table through .j2 file
        return render_template('venues.j2', venues=venue_data)

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

#artists Page
@app.route("/artists")
def artists():
    return render_template("artists.html")

# customers Page
@app.route("/customers", methods=["GET", "POST"])
def customers():
    # READ
    if request.method == 'GET':
        # SQL select Venues table data
        query = 'SELECT * FROM Customers;'
        customer_data = connect(query)
        # render table through .j2 file
        return render_template('customers.j2', customers=customer_data)

    # CREATE
    elif request.method == 'POST':
         # user clicks 'new'
        if request.form.get('insert_customer'):
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            phone_number = request.form['phone_number']
            # insert new row into Venues
            query = 'INSERT INTO Customers (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s);'
            values = (first_name, last_name, email, phone_number)
            connect(query, values)
            # redirect to /venues
            return redirect("/customers")
        
        if request.form["method"] == "put":
            customer_id = int(request.form["customer_id"])
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            phone_number = request.form["phone_number"]

            command = "UPDATE Customers SET first_name = %s, last_name = %s, email = %s, phone_number = %s WHERE customer_id = %s;"
            values = (first_name, last_name, email, phone_number, customer_id)
            connect(command, values)
            return redirect("/customers")
        
        if request.form["method"] == "delete":
            customer_id = int(request.form["customer_id"])

            command = "DELETE FROM Customers WHERE customer_id = %s"
            values = (customer_id,)
            connect(command, values)
            return redirect("/customers")

# concerts Page
@app.route("/concerts", methods=["GET", "POST"])
def concerts():
    # READ
    if request.method == 'GET':
        # SQL select Venues table data
        query = 'SELECT * FROM Concerts;'
        concert_data = connect(query)
        query = 'SELECT artist_id, artist_name from Artists;'
        artist_data = connect(query)
        query = 'SELECT venue_id, address from Venues;'
        venue_data = connect(query)
        # render table through .j2 file
        print(concert_data)
        print(artist_data)
        print(venue_data)
        return render_template('concerts.j2', concerts=concert_data, artists=artist_data, venues=venue_data)

    # CREATE
    elif request.method == 'POST':
         # user clicks 'new'
        if request.form.get('insert_concert'):
            date = request.form['date']
            time = request.form['time']
            venue_id = int(request.form['venue_id'])
            artist_id = int(request.form['artist_id'])
            # insert new row into Venues
            query = 'INSERT INTO Concerts (date, time, venue_id, artist_id) VALUES (%s, %s, %s, %s);'
            values = (date, time, venue_id, artist_id)
            connect(query, values)
            # redirect to /venues
            return redirect("/concerts")
        
        if request.form["method"] == "put":
            concert_id = int(request.form["concert_id"])
            date = request.form["date"]
            time = request.form["time"]
            venue_id = int(request.form["venue_id"])
            artist_id = int(request.form["artist_id"])

            command = "UPDATE Concerts SET date = %s, time = %s, venue_id = %s, artist_id = %s WHERE concert_id = %s;"
            values = (date, time, venue_id, artist_id, concert_id)
            connect(command, values)
            return redirect("/concerts")
        
        if request.form["method"] == "delete":
            concert_id = int(request.form["concert_id"])

            command = "DELETE FROM Concerts WHERE concert_id = %s"
            values = (concert_id,)
            connect(command, values)
            return redirect("/concerts")

# ticketsales Page
@app.route("/ticketsales")
def ticketsales():
    return render_template("ticketsales.html")

# intersection Page
@app.route("/concerts_ticketsales", methods=["GET", "POST"])
def concerts_ticketsales():
    # READ
    if request.method == 'GET':
        # SQL select Venues table data
        query = 'SELECT * FROM Concerts_TicketSales;'
        sale_data = connect(query)
        query = 'SELECT sale_number FROM TicketSales'
        ticket_data = connect(query)
        query = 'SELECT concert_id FROM Concerts'
        concert_data = connect(query)
        # render table through .j2 file
        return render_template('concerts_ticketsales.j2', concert_sales=sale_data, 
                               tickets=ticket_data, concerts=concert_data)

    # CREATE
    elif request.method == 'POST':
         # user clicks 'new'
        if request.form.get('insert_concert_sale'):
            sale_number = request.form['sale_number']
            concert_id = request.form['concert_id']
            # insert new row into Venues
            query = 'INSERT INTO Concerts_TicketSales (sale_number, concert_id) VALUES (%s, %s);'
            values = (sale_number, concert_id)
            connect(query, values)
            # redirect to /venues
            return redirect("/concerts_ticketsales")
        
        if request.form["method"] == "put":
            concert_sale_id = int(request.form["concert_sale_id"])
            sale_number = int(request.form["sale_number"])
            concert_id = int(request.form["concert_id"])

            command = "UPDATE Concerts_TicketSales SET sale_number = %s, concert_id = %s WHERE concert_sale_id = %s;"
            values = (sale_number, concert_id, concert_sale_id)
            connect(command, values)
            return redirect("/concerts_ticketsales")
        
        if request.form["method"] == "delete":
            concert_sale_id = int(request.form["concert_sale_id"])

            command = "DELETE FROM Concerts_TicketSales WHERE concert_sale_id = %s"
            values = (concert_sale_id,)
            connect(command, values)
            return redirect("/concerts_ticketsales")

if __name__ == "__main__":
    app.run(debug=True, port=port_number)
