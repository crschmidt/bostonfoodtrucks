#!/bin/sh

http_proxy="" wget -O foodtrucklocs.js "http://www.cityofboston.gov/business/mobile/initFoodTrucks.js"
echo "console.log(JSON.stringify(Locations));" >> foodtrucklocs.js
node foodtrucklocs.js > locations.js
http_proxy="" python scrape.py > truckinfo.json
