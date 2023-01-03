from typing import Dict, List, Optional, Tuple, Union


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
    self.l = l
  
  def __repr__(self) -> str:
    return f"BBOX({self.min_long}, {self.min_lat}, {self.max_long}, {self.max_lat})"

  def __str__(self) -> str:
    return f"BBOX({self.min_long}, {self.min_lat}, {self.max_long}, {self.max_lat})"



def aggregate_bbox(l: List) -> BBOX:
  """
  Aggregates list of bboxes (picks up "furthest" of each coordinate)
  bbox: [min Longitude , min Latitude , max Longitude , max Latitude]
  Longitude: east west position range: -180.0 and 180.0
  Latitude: south north position range: -90.0 and 90.0
  """
  # starting values
  _min_long = 200.0
  _max_long = -200.0
  _min_lat = 100.0
  _max_lat = -100.0

  # for each bbox 
  for b in l:
    if b[0] < _min_long:
      _min_long = b[0]
    if b[1] < _min_lat:
      _min_lat = b[1]
    if b[2] > _max_long:
      _max_long = b[2]
    if b[3] > _max_lat:
      _max_lat = b[3]

  # results list
  r = [_min_long, _min_lat, _max_long, _max_lat]
  bbox_r = BBOX(r)
  return bbox_r



def compare_bbox(l1: Union[List, BBOX], l2: Union[List, BBOX]) -> str:
  """
  Compares bboxes and checks inclusion/exclusion/intersection
  bbox: [min Longitude , min Latitude , max Longitude , max Latitude]
  Longitude: east west position range: -180.0 and 180.0
  Latitude: south north position range: -90.0 and 90.0
  """
  state = ""

  if isinstance(l1, list):
    b1 = BBOX(l1)
  elif isinstance(l1, BBOX):
    b1 = l1
  else:
    raise ValueError("Provided wrong value for l1 in compare_bbox")

  if isinstance(l2, list):
    b2 = BBOX(l2)
  elif isinstance(l2, BBOX):
    b2 = l2
  else:
    raise ValueError("Provided wrong value for l2 in compare_bbox")


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

  # print(f"BBOX comparison state: {state}")
  return state

