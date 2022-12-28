# Reading natural earth data using...

python and js I guess?

# data from

https://www.naturalearthdata.com/downloads/

# start server
source ./venv/bin/activate
uvicorn main:app --reload
http://127.0.0.1:8000


# will be useful...
https://www.sitepoint.com/how-to-translate-from-dom-to-svg-coordinates-and-back-again/
https://www.petercollingridge.co.uk/tutorials/svg/interactive/dragging/

# todo:
- different color for rivers lines
- make rivers non selectable
- show rivers based on the region selected
- make smarter bbox in merge_gjons
- show cities above certain population/area
- figure out proper zooming of svg elements
- figure out proper translation of svg elements
- for rivers and cities will need the list of countries and their coordinates to select correct rivers/cities
