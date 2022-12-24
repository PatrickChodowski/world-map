from gps import GPS
# g_countries = GPS("ne_50m_admin_0_countries")
# g_cities = GPS("ne_50m_populated_places")
g_rivers = GPS("ne_50m_rivers_lake_centerlines_scale_rank")

g_rivers.copy_csv()

# gj_pol = g_countries.select_geojson(names=['Poland'])
# gj_war = g_cities.select_geojson(names=['Warsaw'])

# gjons = list()
# gjons.append(gj_pol)



# print(gj_pol['type'])
# print(gj_war['type'])

# print(gj_pol.keys())
# print(gj_war.keys())

# if (gj_pol['type'] == "FeatureCollection") & ('features' in gj_pol):
#   print('yes')