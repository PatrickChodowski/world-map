from gps import GPS
from bbox_utils import compare_bbox, aggregate_bbox
import pandas as pd

g_countries = GPS("ne_50m_admin_0_countries")
# g_cities = GPS("ne_50m_populated_places")
g_rivers = GPS("ne_50m_rivers_lake_centerlines_scale_rank")

# map set of objects to another set objects:


g_countries.select_geojson(names=['world'])
countries = g_countries.extract_props()
countries_bbox = g_countries.extract_bbox()

g_rivers.select_geojson(names=['world'])
rivers = g_rivers.extract_props(prop_name='NAME')
rivers_bbox = g_rivers.extract_bbox_list()


countries_df = pd.DataFrame(zip(countries, countries_bbox), columns=['country_name', 'country_bbox']).sort_values('country_name', ignore_index=True)
rivers_df = pd.DataFrame(zip(rivers, rivers_bbox), columns=['river_name', 'river_bbox'])
rivers_bbox_df = rivers_df.groupby(by='river_name').agg({'river_bbox': [aggregate_bbox]}).reset_index()
rivers_bbox_df.columns = ["river_name", "river_bbox"]
rivers_bbox_dicts = rivers_bbox_df.to_dict(orient="records")

# bb1 = rivers_bbox_dicts[0]['river_bbox']
# bb2 = countries_df['country_bbox'][0]
# print(bb1)
# print(bb2)
# compare_bbox(bb1, bb2)

for rb in rivers_bbox_dicts:
  for index, country_row in countries_df.iterrows():
    res = compare_bbox(rb['river_bbox'], country_row['country_bbox'])
    if res in ['b1_inside']:
      print(f"River {rb['river_name']} belongs to {country_row['country_name']}")

#sprawdz czemu wszystko sie mapuje do usa, rosji, francji