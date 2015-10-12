from django.contrib.gis.db import models

class Geo(models.Model):
    statefp = models.CharField(max_length=2)
    countyfp = models.CharField(max_length=3)
    countyns = models.CharField(max_length=8)
    geoid = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    namelsad = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    classfp = models.CharField(max_length=2)
    mtfcc = models.CharField(max_length=5)
    csafp = models.CharField(max_length=3)
    cbsafp = models.CharField(max_length=5)
    metdivfp = models.CharField(max_length=5)
    funcstat = models.CharField(max_length=1)
    aland = models.FloatField()
    awater = models.FloatField()
    intptlat = models.CharField(max_length=11) #centlat
    intptlon = models.CharField(max_length=12) #centlon
    geom = models.MultiPolygonField(srid=-1)
    objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for Geo model
geo_mapping = {
    'statefp' : 'STATEFP',
    'countyfp' : 'COUNTYFP',
    'countyns' : 'COUNTYNS',
    'geoid' : 'GEOID',
    'name' : 'NAME',
    'namelsad' : 'NAMELSAD',
    'lsad' : 'LSAD',
    'classfp' : 'CLASSFP',
    'mtfcc' : 'MTFCC',
    'csafp' : 'CSAFP',
    'cbsafp' : 'CBSAFP',
    'metdivfp' : 'METDIVFP',
    'funcstat' : 'FUNCSTAT',
    'aland' : 'ALAND',
    'awater' : 'AWATER',
    'intptlat' : 'INTPTLAT',
    'intptlon' : 'INTPTLON',
    'geom' : 'MULTIPOLYGON',
}
