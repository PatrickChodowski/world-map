from gps import GPS
from fastapi import FastAPI
app = FastAPI()

MAP_NAME = "ne_50m_admin_0_countries"
g = GPS(MAP_NAME)
cntrs = g.list_countries()

@app.get("/")
async def root():
    return {"Countries": cntrs}
