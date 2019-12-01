from flask import Flask, render_template, request
from src.core.flights.flights import HermesFlights
import os

def root_dir():
  return (os.path.dirname(__file__)).replace('\\', '/')

def static_file():
    return (os.path.dirname(__file__)).replace('\\', '/') + "/assets"

app = Flask(__name__,template_folder=root_dir(), static_folder=static_file(),root_path=root_dir())

@app.route('/')
def index():
  # print(root_dir())
  return render_template("index.html")

@app.route('/get-flights/')
def my_link():
  fl = HermesFlights()
  return fl.getFlightData("BUF-sky", "2019-12-06")

@app.route('/menu.html')
def menu():
    return render_template("menu.html")

@app.route('/flights.html')
def flights():
    return render_template("flights.html")

@app.route('/hotels.html')
def hotels():
    return render_template("hotels.html")

@app.route('/landmarks.html')
def landmarks():
    return render_template("landmarks.html")


if __name__ == '__main__':
  app.run(debug=True)
