
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


class BBOX:
  def __init__(self, l: List[float]) -> None:
    """
    bbox: [min Longitude , min Latitude , max Longitude , max Latitude]
    Longitude: east west position range: -180.0 and 180.0
    Latitude: south north position range: -90.0 and 90.0
    """
    self.min_long = l[0]
    self.min_lat = l[1]
    self.max_long = l[2]
    self.max_lat = l[3]
    self.h = self.max_lat - self.min_lat
    self.w = self.max_long - self.min_long


COLS = dict()
COLS['ne_50m_admin_0_countries'] = ["SOVEREIGNT", "TYPE", "ADMIN", "ADM0_A3", "GEOUNIT", "GU_A3", "SUBUNIT", 
                                    "NAME", "NAME_LONG", "ABBREV", "POSTAL", "FORMAL_EN", "POP_EST", "GDP_MD","ECONOMY", 
                                    "INCOME_GRP", "ISO_A2", "ISO_A3", "CONTINENT", "REGION_UN", "SUBREGION", "REGION_WB", 
                                    "LABEL_X", "LABEL_Y", "NAME_EN", "GEOMETRY"]
COLS['ne_50m_populated_places'] = ['NAME', 'SOV0NAME','LATITUDE','LONGITUDE','NAME_EN', 'ADM0NAME' ,'GEOMETRY']
COLS['ne_50m_rivers_lake_centerlines_scale_rank'] = ['NAME', 'NAME_EN', 'LABEL', 'GEOMETRY']


FILTER_COLS = dict()
FILTER_COLS['ne_50m_admin_0_countries'] = ["SOVEREIGNT", "TYPE", "ADMIN", "GEOUNIT", "SUBUNIT", "NAME", "NAME_LONG", "CONTINENT", "REGION_UN", "SUBREGION", "ISO_A3"]
FILTER_COLS['ne_50m_populated_places'] = ['NAME_EN', 'SOV0NAME']
FILTER_COLS['ne_50m_rivers_lake_centerlines_scale_rank'] = ['NAME', 'NAME_EN', 'LABEL']


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


def extract_props(gc: Optional[Dict], prop_name: str = 'SOVEREIGNT') -> List:
  """
  Extract list of properties from gps object data
  """
  list_of_props = list()
  if gc is not None:
    for v in gc['features']:
      if prop_name in v['properties']:
        list_of_props.append(v['properties'][prop_name])
  return list_of_props


def extract_bbox(gc: Optional[Dict]) -> List:
  """
  Extract list of bboxes from gps object data
  """
  list_of_bbox = list()
  if gc is not None:
    for v in gc['features']:
      list_of_bbox.append(v['bbox'])
  return list_of_bbox



def compare_bbox(l1: List, l2: List) -> str:
  """
  Compares bboxes and checks inclusion/exclusion/intersection
  bbox: [min Longitude , min Latitude , max Longitude , max Latitude]
  Longitude: east west position range: -180.0 and 180.0
  Latitude: south north position range: -90.0 and 90.0
  """
  state = ""

  b1 = BBOX(l1)
  b2 = BBOX(l2)

  if ((b1.min_long < b2.min_long + b2.w) & (b1.min_long + b1.w > b2.min_long) & (b1.min_lat < b2.min_lat + b2.h) &(b1.h + b1.min_lat > b2.min_lat)):
    state = "collision"
  else:
    state = "exclusion"

  # check if b1 absolutely in b2
  if ((b1.min_long >= b2.min_long) & (b1.max_long <= b2.max_long) & (b1.min_lat >= b2.min_lat) & (b1.max_lat <= b2.max_lat)):
    state = "b1_inside"

  # check if b2 absolutely in b1
  if ((b2.min_long >= b1.min_long) & (b2.max_long <= b1.max_long) & (b2.min_lat >= b1.min_lat) & (b2.max_lat <= b1.max_lat)):
    state = "b2_inside"

  print(f"BBOX comparison state: {state}")
  return state


