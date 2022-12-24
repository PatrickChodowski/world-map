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
- filter to show cities
- filter to show rivers
- different color for rivers lines
- make rivers non selectable
- show cities based on the region selected
- show rivers based on the region selected
- pass additional data to frontend
- make smarter bbox in merge_gjons
- show cities above certain population/area
- build whole setting panel and move it to different component
- figure out proper zooming of svg elements
- figure out proper translation of svg elements
