from gps import GPS
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class SelectData(BaseModel):
  country: str

app = FastAPI()
MAP_NAME = "ne_50m_admin_0_countries"
g = GPS(MAP_NAME)

@app.post("/select")
async def select(data: SelectData):
  # print(data.country)
  countries = data.country.split(";")
  gj = g.select_geojson(names=countries)
  return {"data": gj}


app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=False,
                   allow_methods=["POST"],
                   allow_headers=["*"],)
