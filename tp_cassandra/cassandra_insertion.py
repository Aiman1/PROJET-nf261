from cassandra.cluster import Cluster
cluster = Cluster()

import csv
import io
import gzip
from datetime import datetime


datapath = "/data/201409-citibike-tripdata.csv.gz"
{'birth year': '1980', 'usertype': 'Subscriber', 'start station name': 'Centre St & Worth St',
 'starttime': '9/1/2014 00:00:25', 'bikeid': '15941', 'end station name': 'W 49 St & 8 Ave', 
 'start station longitude': '-74.00234482', 'start station latitude': '40.71494807', 'end station longitude': '-73.98788205', 'tripduration': '2828',
 'end station id': '450', 'end station latitude': '40.76227205', 'stoptime': '9/1/2014 00:47:33', 'gender': '1', 'start station id': '386'}
with cluster.connect('pacetheo') as session:
    session.execute("""
            CREATE TABLE bikes (id int, start_station_longitude float, start_station_latitude float,
            end_station_longitude float, end_station_latitude float,date text,  )
        """)
        with io.TextIOWrapper(gzip.open(datapath)) as dataStream:
        csv_reader = csv.DictReader(dataStream)
        for r in csv_reader:
            raw_date = r["starttime"]
            my_datetime = datetime.strptime(raw_date, '%m/%d/%Y %H:%M:%S')
            my_date = str(my_datetime.date())
            year,my_week,my_weekday = my_datetime.isocalendar()
            my_month = my_datetime.month
            my_row = {'starttime':r['starttime'], 'start station longitude':r['start station longitude'], 
            'end station longitude': r['end station longitude'], 'stoptime':r['stoptime'], 'end station latitude':r['end station latitude'],
             'start station latitude': r['start station latitude'],'date':my_date, 'week':my_week, 'weekday':my_weekday, 'month':my_month }
            print(my_row)
            session.execute("INSERT ")
            break;        