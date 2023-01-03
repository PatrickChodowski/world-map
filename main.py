from gps import GPS
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from utils import merge_gjons

class SelectData(BaseModel):
  country: str
  show_cities: bool
  show_rivers: bool

app = FastAPI()
g_countries = GPS("ne_50m_admin_0_countries")
g_cities = GPS("ne_50m_populated_places")
g_rivers = GPS("ne_50m_rivers_lake_centerlines_scale_rank")
gjons = list()

@app.post("/select")
async def select(data: SelectData):
  countries = data.country.split(";")
  gjons = list()
  gjons.append(g_countries.select_geojson(names=countries))
  list_of_countries = g_countries.extract_props(prop_name = 'SOVEREIGNT')
  if data.show_cities:
    gjons.append(g_cities.select_geojson(names=list_of_countries))
  if data.show_rivers:
    gjons.append(g_rivers.select_geojson(names=countries))
  gj = merge_gjons(gjons)
  return {"data": gj}


app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=False,
                   allow_methods=["POST"],
                   allow_headers=["*"],)
