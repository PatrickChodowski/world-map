from gps import GPS
g_countries = GPS("ne_50m_admin_0_countries")
# g_cities = GPS("ne_50m_populated_places")
# g_rivers = GPS("ne_50m_rivers_lake_centerlines_scale_rank")

# g_rivers.copy_csv()

gj_pol = g_countries.select_geojson(names=['Poland','Italy'])
# gj_war = g_cities.select_geojson(names=['Warsaw'])

# print(gj_pol)
# print(gj_pol['features'].__len__())

# each feature has properties dictionary