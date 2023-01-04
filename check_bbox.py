from gps import GPS
from bbox_utils import compare_bbox, aggregate_bbox
import pandas as pd
import shapely.geometry as sg

g_countries = GPS("ne_50m_admin_0_countries")
g_rivers = GPS("ne_50m_rivers_lake_centerlines_scale_rank")


rivers_geoj = g_rivers.select_geojson(names=['world'])
vistula = g_rivers.extract_feature_by_props('NAME', 'Vistula')

poland = g_countries.extract_feature_by_props('ADMIN', 'Poland')
poland_coords = poland[0]['geometry']['coordinates'][0]

river_coords = vistula[0]['geometry']['coordinates']
river_coords

# check if belongs to polygon:

river_coords_line = sg.LineString(river_coords)
poland_coords_poly = sg.Polygon(poland_coords)

# :D its that simple!
river_coords_line.intersects(poland_coords_poly)
















# for f in vistula:
#   if f['geometry']['type'] == "LineString":
#     f_coords = f['geometry']['coordinates']
#     print(f_coords)

# take only first set of coordinates

world_geoj = g_countries.select_geojson(names=['world'])



a = g_countries.extract_feature_by_props('ADMIN', 'United States of America')
# print(a[0].keys())

len(a)

geo_type = a[0]['geometry']['type']
coords0 = a[0]['geometry']['coordinates']
coords = coords0[0]
coords.__len__()


 # hmm, length of the list, number of polygons?



# france bbox: [-61.794091796874994, -21.36904296875001, 55.83906250000001, 51.097119140625]}
# poland bbox: [14.128613281250011, 49.020751953125, 24.105761718750017, 54.838183593749996]
# usa bbox: [-178.19453125, 18.963916015625003, 179.77998046875, 71.407666015625] -- almost whole globe width!!!


# need to check single polygons? ugh




