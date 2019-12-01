from flask import Flask, render_template, request
from src.core.flights.flights import HermesFlights
import os

"""
Author: Javier Falca
Date modified: 10/20/2019
Description: Creates a path to html files from the OS directory structure
Returns: Path to html files
"""
def root_dir():
  return os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')[:-15]

app = Flask(__name__,template_folder=root_dir(), static_folder=root_dir())

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

  return fl.getFlightData("BUF-sky", "2019-11-26")

if __name__ == '__main__':
  app.run(debug=True)
