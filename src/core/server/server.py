from flask import Flask, render_template
from src.core.flights.flights import HermesFlights
app = Flask(__name__,template_folder='C:/Users/jafal/PycharmProjects/442projects-sjdf/', static_folder='C:/Users/jafal/PycharmProjects/442projects-sjdf/')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/get-flights/')
def my_link():
  fl = HermesFlights()
  return fl.getFlightData("BUF-sky", "2019-10-23")

if __name__ == '__main__':
  app.run(debug=True)