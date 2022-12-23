from gps import GPS
import shapely
MAP_NAME = "ne_50m_admin_0_countries"
g = GPS(MAP_NAME)
import json

# g.plot("NAME", ["Poland", "Philippines", "United Arab Emirates"])
# g.plot("CONTINENT", ["Africa"])
# g.plot()

# data = g.select("ADMIN", ["Italy"])
# p = data[0]['geometry']
# g._convert_polygon_data(p)

# cntrs = ["Italy", "Poland"]
c = "Poland"
data = g.select("ADMIN", [c])
data_df = g.select_df("ADMIN", [c])
a = data[0]['geometry']
a2 = data_df['geometry']

ja = json.dumps(shapely.geometry.mapping(a))
ja2 = json.dumps(shapely.geometry.mapping(a2))

print(ja)

print(ja2)
# convert to geojson
# ja = json.dumps(shapely.geometry.mapping(a))
# print(ja)