from gps import GPS
from utils import extract_country_data

g_countries = GPS("ne_50m_admin_0_countries")
g_cities = GPS("ne_50m_populated_places")
g_rivers = GPS("ne_50m_rivers_lake_centerlines_scale_rank")

gj_pol = g_countries.select_geojson(names=['Poland','Italy'])



extract_country_data(gj_pol)