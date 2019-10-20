from flask import Flask, render_template, request
from src.core.flights.flights import HermesFlights
from selenium import webdriver
import os


def root_dir():
  return os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')[:-15]

app = Flask(__name__,template_folder=root_dir(), static_folder=root_dir())

@app.route('/')
def index():
  # print(root_dir()[:-15])

  return render_template('index.html')

@app.route('/get-flights/')
def my_link():
  fl = HermesFlights()

  return fl.getFlightData("BUF-sky", "2019-10-23")

if __name__ == '__main__':
  app.run(debug=True)