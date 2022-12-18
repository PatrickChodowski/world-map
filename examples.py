from gps import GPS


MAP_NAME = "ne_50m_admin_0_countries"

g = GPS(MAP_NAME)

# full map
g.plot()

# single plot
g.plot_single(0)

# multiple countries
_i = list(range(10, 50, 1))
g.plot_multiple(_i)
