import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my Climate page!"

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("JSON representation of dictionary")
    return "Welcome to my Precipitation page!"

@app.route("/api/v1.0/stations")
def stations():
    print("JSON list of stations from the dataset")
    return "Welcome to my Stations page!"

@app.route("/api/v1.0/tobs")
def tobs():
    print("JSON list of temperature observations for the previous year")
    return "Welcome to my Tobs page!"

@app.route("/api/v1.0/<start>")
def start():
    print("Server received request for 'About' page...")
    return "Welcome to my Start page!"

@app.route("/api/v1.0/<start>/<end>")
def end():
    print("Server received request for 'About' page...")
    return "Welcome to my End page!"


if __name__ == "__main__":
    app.run(debug=True)
