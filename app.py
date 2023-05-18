from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)
port_number = 27205

# index Page
@app.route("/")
def index():
    return render_template("index.html")

# venues Page
@app.route("/venues")
def venues():
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
