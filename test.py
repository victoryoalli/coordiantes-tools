from shapely.geometry import shape,Point, Polygon
import fiona
from collections import OrderedDict


print(fiona.__file__)

input = fiona.open("out.shp","r")

print "ID,\t TYPE,\t LAT,\t LONG\n"
for feat in input:       
	ls = shape(feat['geometry'])

	print feat
#	print "\nPROPERTIES"
#	print feat['properties']['OBJECTID']
#	print feat['properties']['ENTIDAD']
#	print "\n COOR"
	for c in feat['geometry']['coordinates']:
		p = Point(c)
		print("%s,%s,%s,%s" % (feat['id'], feat['properties']['ENTIDAD'],p.y,p.x))
#		print p.x
#		print p.y

	print "\n"
		
#import pyproj

#print shape.schema
#{'geometry': 'LineString', 'properties': OrderedDict([(u'FID', 'float:11')])}


# original projection
#p = pyproj.Proj("+proj=stere +lat_0=90 +lat_ts=60 +lon_0=-105 +k=90 +x_0=0 +y_0=0 +a=6371200 +b=6371200 +units=m +no_defs")
#p = pyproj.Proj("+proj=lcc +lat_1=38.69259533705237 +lat_2=39.02625053604863 +lat_0=40 +lon_0=-77.03638889 +x_0=0 +y_0=0 +ellps=GRS80 +units=m +no_defs")
#p = pyproj.Proj(init='epsg:102009')
#p = pyproj.Proj(init='epsg:4326')
#p = pyproj.Proj(init="epsg:102009")
# resulting projection, WGS84, long, lat
#outProj =pyproj.Proj(init='epsg:4326')
#outProj =pyproj.Proj("+proj=longlat +ellps=WGS84 +no_defs")

#x1,y1 = [27.3201814612917, -109.690983032217]
#x1,y1 = [3856491.15003532,950400.613083786]
#lon,lat = pyproj.transform(p,outProj,x1,y1)
#print lon, lat
#(104.06918350995736, 53.539892485824495)
