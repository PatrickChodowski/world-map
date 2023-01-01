import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import shapely.geometry as sg
import shapely.ops as so
import shapely
import json
from typing import List, Optional, Dict
import numpy as np
from utils import COLS, FILTER_COLS


class GPS:
  def __init__(self, map_name: str) -> None:
    self.map_name = map_name

    # other variables
    self.shapefile = None
    self.fig_width = 16
    self.fig_height = 12

    self._read_file()
    self._index = self._make_index()

  def _read_file(self) -> None:
    """
    Reads shapefile data
    """
    df = gpd.read_file(f"./data/{self.map_name}/{self.map_name}.shp")
    df.columns = df.columns.str.upper()
    self.shapefile = df[~pd.isnull(df['GEOMETRY'])]

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
    poly = self.shapefile['GEOMETRY'][index]
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


  def select_geojson(self, names: List[str]) -> Optional[Dict]:
    """
    Main data selection function
    """
    if (names is None) | (names.__len__() == 0) | (names == ['']):
      d = None
    elif names == ['world']:
      d = self.shapefile[COLS[self.map_name]]
    else:
      list_of_indices = self._filter_data(names)
      d = self.shapefile[COLS[self.map_name]].iloc[list_of_indices]

    if d is not None:
      geoj = json.loads(json.dumps(shapely.geometry.mapping(d['GEOMETRY'])))
      if np.isnan(geoj['bbox']).any():
        return None
      else:
        for index, (_, row) in enumerate(d.iterrows()):
          del row['GEOMETRY']
          geoj['features'][index]['properties'] = row
        return geoj
    else:
      return None

  def copy_csv(self) -> None:
    self.shapefile.to_csv("./data/temp.csv")


  def _make_index(self) -> Dict:
    """
    Creates the index after loading the shapefile data
    """
    a = self.shapefile[FILTER_COLS[self.map_name]].reset_index(drop=False)
    b = pd.melt(frame=a, id_vars="index")
    c = b.groupby(['value']).agg({'index': lambda x: list(set(x)), 'variable': lambda x: list(set(x))})
    d = c.to_dict(orient="index")
    return d
