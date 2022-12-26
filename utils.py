
from typing import Dict, List

COLS = dict()
COLS['ne_50m_admin_0_countries'] = ["SOVEREIGNT", "TYPE", "ADMIN", "ADM0_A3", "GEOUNIT", "GU_A3", "SUBUNIT", 
                                    "NAME", "NAME_LONG", "ABBREV", "POSTAL", "FORMAL_EN", "POP_EST", "GDP_MD","ECONOMY", 
                                    "INCOME_GRP", "ISO_A2", "ISO_A3", "CONTINENT", "REGION_UN", "SUBREGION", "REGION_WB", 
                                    "LABEL_X", "LABEL_Y", "NAME_EN", "geometry"]
COLS['ne_50m_populated_places'] = ['NAME', 'SOV0NAME','LATITUDE','LONGITUDE','NAME_EN', 'ADM0NAME' ,'geometry']
COLS['ne_50m_rivers_lake_centerlines_scale_rank'] = ['name', 'name_en', 'label', 'geometry']


FILTER_COLS = dict()
FILTER_COLS['ne_50m_admin_0_countries'] = ["SOVEREIGNT", "TYPE", "ADMIN", "GEOUNIT", "SUBUNIT", "NAME", "NAME_LONG", "CONTINENT", "REGION_UN", "SUBREGION", "ISO_A3"]
FILTER_COLS['ne_50m_populated_places'] = ['NAME_EN']
FILTER_COLS['ne_50m_rivers_lake_centerlines_scale_rank'] = ['name','name_en','label']


def merge_gjons(gjons: List[Dict]) -> Dict:
  """
  Function to merge list of geojsons into one geojson
  """
  # main geojsons
  d = dict()
  d['type'] = 'FeatureCollection'
  d['features'] = list()
  d['bbox'] = list()

  if gjons[0] is not None:
    for g in gjons:
      # print(g)
      if g is not None:
        if ((g['type'] == "FeatureCollection") & ('features' in g)  & ('bbox' in g)):
          d['features'].extend(g['features'])

    # too lazy to solve this right now
    d['bbox']  = gjons[0]['bbox']

  return d
