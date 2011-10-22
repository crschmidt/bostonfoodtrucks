import BeautifulSoup
import urllib
import json

soup = BeautifulSoup.BeautifulSoup(urllib.urlopen("http://www.cityofboston.gov/business/mobile/schedule-app.asp?v=1").read())
stops = soup.findAll("tr")[1:]
#print len(stops)
data = {
    'locations': json.load(open("locations.js"))
}
locs_array = []
for k, v in data['locations'].items():
        v['id'] = k
	locs_array.append(v)
data['locations_array'] = locs_array
stop_data = []


for stop in stops:
    s = {
        'name': stop.findAll("td")[1].findAll("a")[0].text,
        'day': stop.findAll("td")[2].text,
        'time': stop.findAll("td")[3].text,
        'location': stop.findAll("td")[4].findChildren()[0].nextSibling,
        }
    mapinfo = stop.findAll("td")[4].findChildren()[0].text
    if mapinfo:
        #print mapinfo
        mapinfo = str(mapinfo).split('"')[1]
    s['mapinfo'] = mapinfo    
    stop_data.append(s)
data['stops'] = stop_data
print json.dumps(data)
