import geojson
import tempfiile

def write_json(self, features):
   # feature is a shapely geometry feature
   geom_in_geojson = geojson.Feature(geometry=features, properties={})
   tmp_file = tempfile.mkstemp(suffix='.geojson')
   with open(tmp_file[1], 'w') as outfile:
      geojson.dump(geom_in_geojson, outfile)
   return tmp_file[1]