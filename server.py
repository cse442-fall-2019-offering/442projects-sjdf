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
  return fl.getFlightData("BUF-sky", "2019-11-10")

@app.route('/menu.html')
def menu():
    return render_template("menu.html")


if __name__ == '__main__':
  app.run(debug=True)
