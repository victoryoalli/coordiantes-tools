from shapely.geometry import shape,Point, Polygon
import fiona
from collections import OrderedDict

input = fiona.open("data/PlantaGeneradora-wgs84.shp","r")

print "ID,TYPE,LAT,LONG"
for feat in input:       
	#print feat
	p = shape(feat['geometry'])
	#print ls
	print("%s,'%s',%s,%s" % (feat['id'], feat['properties']['ENTIDAD'],p.y,p.x))
