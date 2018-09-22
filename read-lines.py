from shapely.geometry import shape,Point, Polygon
import fiona
from collections import OrderedDict

input = fiona.open("data/Archivo-wgs84.shp","r")

print "ID,TYPE,LAT,LONG"
for feat in input:       
	ls = shape(feat['geometry'])

	for c in feat['geometry']['coordinates']:
		p = Point(c)
		print("%s,'%s',%s,%s" % (feat['id'], feat['properties']['ENTIDAD'],p.y,p.x))

