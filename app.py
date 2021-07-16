import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)
engine = create_engine(f"sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect = True)

Measurement = Base.classes.measurement
Station = Base.classes.station



# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return '''Welcome to my Climate page!: 
<ul> 
<li><a href = "/api/v1.0/precipitation" >precipitation</li>
<li><a href = "/api/v1.0/stations" >stations</li>
<li><a href = "/api/v1.0/tobs" >tobs</a></li>
<li>  " Add  '/api/v1.0/' to url followed by date YYYY-MM-DD " </li>
<li><a href = "/api/v1.0/<start>/<end>" > <start>/<end> </li>
</ul>

'''


@app.route("/api/v1.0/precipitation")
def precipitation(): 
    print("JSON representation of dictionary")
    session = Session(engine)
    precipt_data = session.query(Measurement.date, Measurement.prcp).all()
    return {date: prcp for date, prcp in precipt_data}

@app.route("/api/v1.0/stations")
def stations():
    print("JSON list of stations from the dataset")
    session = Session(engine)
    station_data  = session.query(Station.station, Station.name).all()
    return {station: name for station, name in station_data }
    

@app.route("/api/v1.0/tobs")
def tobs():
    print("JSON list of temperature observations for the previous year")
    session = Session(engine)
    temp_obv = session.query(Measurement.date, Measurement.tobs).all()
    return {date: tobs for date, tobs in temp_obv}

    

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start(start , end = "2017-08-23"):
    print("Server received request for 'About' page...")
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.tobs).filter((Measurement.date >= start) & (Measurement.date <= end )).all()
    return {date:tobs for date, tobs in results }

    


if __name__ == "__main__":
    app.run(debug=True)
