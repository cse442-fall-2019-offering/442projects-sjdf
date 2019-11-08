from flask import Flask, render_template, request, url_for, redirect
from src.core.flights.flights import HermesFlights
import os
import json

"""
Author: Javier Falca
Date modified: 10/20/2019
Description: Creates a path to html files from the OS directory structure
Returns: Path to html files
"""

userData = {}
def root_dir():
    return os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')[:-15]


app = Flask(__name__, template_folder=root_dir(), static_folder=root_dir())

"""
Author: Javier Falca
Date modified: 10/20/2019
Description: Runs a server framework using flask
Returns: Static html files
"""


@app.route('/')
def index():
    # print(root_dir()[:-15])

    return render_template('index.html')


@app.route('/get-flights/')
def my_link():
    fl = HermesFlights()
    return fl.getFlightData("BUF-sky", "2019-10-23")

"""
Author: Florebencia Fils-Aime and Javier Falca
Date modified: 11/6/2019
Description: Uses the post request from the form to get user data
Returns: Static html files
"""
@app.route("/userdata", methods=['GET', 'POST'])  #
def userform():
    if request.method == 'POST':
        location = request.form["location"]
        price = request.form["price"]
        currency = request.form["curr_type"]
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]

        userData["location"] = location
        userData["price"] = price
        userData["currency"] = currency
        userData["start_date"] = start_date
        userData["end_date"] = end_date

        return redirect(url_for('static', filename='flights.html'))
    else:
        return json.dumps(userData)


if __name__ == '__main__':
    app.run(debug=True)
