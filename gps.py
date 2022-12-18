import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import shapely.geometry as sg
import shapely.ops as so
from typing import List


class GPS:
  def __init__(self, map_name: str) -> None:
    self.map_name = map_name

    # other variables
    self.shapefile = None
    self.meta = None
    self.fig_width = 16
    self.fig_height = 12

    self.read_file()
    self.select_data()


  def read_file(self) -> None:
    """
    Reads shapefile data
    """
    self.shapefile = gpd.read_file(f"./data/{self.map_name}/{self.map_name}.shp")


  def list_countries(self) -> List[str]:
    """
    Lists all countries in the file
    """
    l = list(self.shapefile["NAME"].values)
    print(l)
    return l

  def plot(self) -> None:
    """
    Plots whole file
    """
    self.shapefile.plot(figsize=(self.fig_width, self.fig_height))
    plt.show()


  def plot_single(self, index: int) -> None:
    """
    Plots single polygon
    """
    poly = self.shapefile['geometry'][index]
    p = gpd.GeoSeries(poly)
    p.plot(figsize=(self.fig_width, self.fig_height))
    plt.show()


  def plot_multiple(self, indices: List[int]) -> None:
    """
    Plots multiple Polygons together as new shape
    """
    polys = list(self.shapefile['geometry'].iloc[indices])
    new_shape = so.unary_union(polys)
    gpd.GeoSeries(new_shape).plot(figsize=(self.fig_width, self.fig_height))
    plt.show()


  def select_data(self) -> None:
    """
    Creates subset of data in pandas for filtering
    """
    cols = ["SOVEREIGNT", "TYPE", "ADMIN", "ADM0_A3", "GEOUNIT", "GU_A3", "SUBUNIT", 
            "NAME", "NAME_LONG", "ABBREV", "POSTAL", "FORMAL_EN", "POP_EST", "GDP_MD","ECONOMY", 
            "INCOME_GRP", "ISO_A2", "ISO_A3", "CONTINENT", "REGION_UN", "SUBREGION", "REGION_WB", "LABEL_X", "LABEL_Y", "NAME_EN"]

    self.meta = self.shapefile[cols]



  def copy_csv(self) -> None:
    self.shapefile.to_csv("temp.csv")