from gps import GPS, FILTER_COLS
MAP_NAME = "ne_50m_admin_0_countries"
g = GPS(MAP_NAME)
import pandas as pd

a = g.shapefile[FILTER_COLS].reset_index(drop=False)
b = pd.melt(frame=a, id_vars="index")
c = b.groupby(['value']).agg({'index': lambda x: list(set(x)), 'variable': lambda x: list(set(x))})
d = c.to_dict(orient="index")
print(d)
print(d.keys())