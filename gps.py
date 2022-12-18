import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import shapely.geometry as sg
import shapely.ops as so
from typing import List, Optional, Dict

COLS = ["SOVEREIGNT", "TYPE", "ADMIN", "ADM0_A3", "GEOUNIT", "GU_A3", "SUBUNIT", 
            "NAME", "NAME_LONG", "ABBREV", "POSTAL", "FORMAL_EN", "POP_EST", "GDP_MD","ECONOMY", 
            "INCOME_GRP", "ISO_A2", "ISO_A3", "CONTINENT", "REGION_UN", "SUBREGION", "REGION_WB", "LABEL_X", "LABEL_Y", "NAME_EN", "geometry"]

class GPS:
  def __init__(self, map_name: str) -> None:
    self.map_name = map_name

    # other variables
    self.shapefile = None
    self.fig_width = 16
    self.fig_height = 12

    self._read_file()


  def _read_file(self) -> None:
    """
    Reads shapefile data
    """
    self.shapefile = gpd.read_file(f"./data/{self.map_name}/{self.map_name}.shp")


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


  def _plot_multiple(self, indices: List[int]) -> None:
    """
    Plots multiple Polygons together as new shape
    """
    polys = list(self.shapefile['geometry'].iloc[indices])
    new_shape = so.unary_union(polys)
    gpd.GeoSeries(new_shape).plot(figsize=(self.fig_width, self.fig_height))
    plt.show()


  def _filter_data(self, attrb_name: str, attrb_values: List[str]) -> List[int]:
    """
    You can filter by column and list of values, returns list of indices. Will plot accordingly
    """
    l = list(self.shapefile.loc[self.shapefile[attrb_name].isin(attrb_values)].index)
    return l


  def plot(self, attrb_name: Optional[str] = None, attrb_values: Optional[List[str]] = None) -> None:
    """
    Main plotting function
    """

    if (attrb_name is None) | (attrb_values is None):
      self._plot_whole()
    else:
      list_of_indices = self._filter_data(attrb_name=attrb_name, attrb_values=attrb_values)

      if len(list_of_indices) == 1:
        self._plot_single(index=list_of_indices[0])
      elif len(list_of_indices) > 1:
        self._plot_multiple(indices=list_of_indices)
      else:
        print(f"Cant plot as list of indices for attrb_name: {attrb_name} and attrb_values: {attrb_values} is [{list_of_indices}]")


  def select(self, attrb_name: Optional[str] = None, attrb_values: Optional[List[str]] = None) -> Dict:
    """
    Main data selection function
    """
    if (attrb_name is None) | (attrb_values is None):
      return self.shapefile[COLS].to_dict(orient="records")
    else:
      list_of_indices = self._filter_data(attrb_name=attrb_name, attrb_values=attrb_values)
      return self.shapefile[COLS].iloc[list_of_indices].to_dict(orient="records")



  # def copy_csv(self) -> None:
  #   self.shapefile.to_csv("temp.csv")