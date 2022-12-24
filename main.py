from gps import GPS
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from utils import merge_gjons

class SelectData(BaseModel):
  country: str

app = FastAPI()
g_countries = GPS("ne_50m_admin_0_countries")
g_cities = GPS("ne_50m_populated_places")
gjons = list()

@app.post("/select")
async def select(data: SelectData):
  countries = data.country.split(";")
  gjons = list()
  gjons.append(g_countries.select_geojson(names=countries))
  gjons.append(g_cities.select_geojson(names=['Warsaw']))
  gj = merge_gjons(gjons)
  return {"data": gj}


app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=False,
                   allow_methods=["POST"],
                   allow_headers=["*"],)
