from gps import GPS
from utils import extract_props, extract_bbox, compare_bbox

g_countries = GPS("ne_50m_admin_0_countries")
# g_cities = GPS("ne_50m_populated_places")
g_rivers = GPS("ne_50m_rivers_lake_centerlines_scale_rank")

# gj_pol = g_countries.select_geojson(names=['Jamaica'])
# vis = g_rivers.select_geojson(names=['Vistula'])
# countries, bboxes = extract_country_data(gj_pol)

# compare_bbox(vis['bbox'], bboxes[0])



# map set of objects to another set objects:


gj_countries = g_countries.select_geojson(names=['world'])
gj_rivers = g_rivers.select_geojson(names=['world'])
countries = extract_props(gj_countries)
countries_bbox = extract_bbox(gj_countries)
rivers = extract_props(gj_rivers, prop_name='NAME')
rivers_bboxes = extract_bbox(gj_rivers)

print(rivers.__len__())
print(rivers_bboxes.__len__())

# for river_name, bb_river in zip(rivers, rivers_bboxes):
#   print(f"River: {river_name} bbox: {bb_river}")
