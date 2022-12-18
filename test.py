from gps import GPS
MAP_NAME = "ne_50m_admin_0_countries"
g = GPS(MAP_NAME)

g.plot("NAME", ["Poland", "Philippines", "United Arab Emirates"])
g.plot("CONTINENT", ["Africa"])
g.plot()
