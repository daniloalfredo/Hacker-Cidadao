import sys
from geojson import Feature, Point, FeatureCollection, Polygon
import json
import geojson
from pprint import pprint

#print(sys.version)

path=r'foo.geojson'

with open(path,'r') as data_file:
    data = json.load(data_file)

feature_collection = FeatureCollection(data['features'])

print feature_collection['features']