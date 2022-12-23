import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import shapely.geometry as sg
import shapely.ops as so
import shapely
import json
from typing import List, Optional, Dict
import numpy as np

COLS = ["SOVEREIGNT", "TYPE", "ADMIN", "ADM0_A3", "GEOUNIT", "GU_A3", "SUBUNIT", 
            "NAME", "NAME_LONG", "ABBREV", "POSTAL", "FORMAL_EN", "POP_EST", "GDP_MD","ECONOMY", 
            "INCOME_GRP", "ISO_A2", "ISO_A3", "CONTINENT", "REGION_UN", "SUBREGION", "REGION_WB", "LABEL_X", "LABEL_Y", "NAME_EN", "geometry"]

FILTER_COLS = ["SOVEREIGNT", "TYPE", "ADMIN", "GEOUNIT", "SUBUNIT", "NAME", "NAME_LONG", "CONTINENT", "REGION_UN", "SUBREGION", "ISO_A3"]

class GPS:
  def __init__(self, map_name: str) -> None:
    self.map_name = map_name

    # other variables
    self.shapefile = None
    self.fig_width = 16
    self.fig_height = 12

    self._read_file()
    self._index = self._make_index()
    # print(self._index)
    # self.copy_csv()

  def _read_file(self) -> None:
    """
    Reads shapefile data
    """
    df = gpd.read_file(f"./data/{self.map_name}/{self.map_name}.shp")
    self.shapefile = df[~pd.isnull(df['geometry'])]


  def list_countries(self) -> List[str]:
    """
    Lists all countries in the file
    """
    l = list(self.shapefile["NAME"].values)
    # print(l)
    return l


  def _plot_whole(self) -> None:
    """
    Plots whole file
    """
    self.shapefile.plot(figsize=(self.fig_width, self.fig_height))
    plt.show()


  def _plot_single(self, index: int) -> None:
    """
    Plots single polygon
    """
    poly = self.shapefile['geometry'][index]
    p = gpd.GeoSeries(poly)
    p.plot(figsize=(self.fig_width, self.fig_height))
    plt.show()


  def _filter_data(self, names: List[str]) -> List[int]:
    """
    You can filter by names of values in the index, returns list of indices. Will plot accordingly
    """
    indices = list()
    for n in names:
      if n in self._index:
        indices.extend(self._index[n]['index'])
    unique_indices = list(set(indices))
    return unique_indices


  def plot(self, names: List[str]) -> None:
    """
    Main plotting function
    """

    if (names is None):
      self._plot_whole()
    else:
      list_of_indices = self._filter_data(names)

      if len(list_of_indices) == 1:
        self._plot_single(index=list_of_indices[0])
      elif len(list_of_indices) > 1:
        self._plot_multiple(indices=list_of_indices)
      else:
        print(f"Cant plot as list of indices for names: {names} is [{list_of_indices}]")


  # def select(self, attrb_name: Optional[str] = None, attrb_values: Optional[List[str]] = None) -> Dict:
  #   """
  #   Main data selection function
  #   """
  #   if (attrb_name is None) | (attrb_values is None):
  #     d = self.shapefile[COLS].to_dict(orient="records")
  #   else:
  #     list_of_indices = self._filter_data(attrb_name=attrb_name, attrb_values=attrb_values)
  #     d = self.shapefile[COLS].iloc[list_of_indices].to_dict(orient="records")

  #   for record in d:
  #     record['geojson'] = json.dumps(shapely.geometry.mapping(record['geometry']))
  #   return d


  # def select_df(self, attrb_name: Optional[str] = None, attrb_values: Optional[List[str]] = None) -> pd.DataFrame:
  #   """
  #   Main data selection function
  #   """
  #   if (attrb_name is None) | (attrb_values is None):
  #     d = self.shapefile[COLS]
  #   else:
  #     list_of_indices = self._filter_data(attrb_name=attrb_name, attrb_values=attrb_values)
  #     d = self.shapefile[COLS].iloc[list_of_indices]

  #   # for index, record in d.iterrows():
  #   #   record['geojson'] = json.dumps(shapely.geometry.mapping(record['geometry']))

  #   record['geojson'] = json.dumps(shapely.geometry.mapping(d['geometry']))
  #   return d


  def select_geojson(self, names: List[str]) -> Optional[Dict]:
    """
    Main data selection function
    """
    if (names is None):
      d = self.shapefile[COLS]
    else:
      list_of_indices = self._filter_data(names)
      d = self.shapefile[COLS].iloc[list_of_indices]

    geoj = json.loads(json.dumps(shapely.geometry.mapping(d['geometry'])))

    if np.isnan(geoj['bbox']).any():
      return None
    else:
      return geoj

  def copy_csv(self) -> None:
    self.shapefile.to_csv("./data/temp.csv")


  def _make_index(self) -> Dict:
    """
    Creates the index after loading the shapefile data
    """
    a = self.shapefile[FILTER_COLS].reset_index(drop=False)
    b = pd.melt(frame=a, id_vars="index")
    c = b.groupby(['value']).agg({'index': lambda x: list(set(x)), 'variable': lambda x: list(set(x))})
    d = c.to_dict(orient="index")
    return d