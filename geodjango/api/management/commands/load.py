from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping
from api.models import Geo, geo_mapping

class Command(BaseCommand):
    help = "Load shapes (tracts, counties, msas) from a shape file."
    shp_file = '/home/vagrant/geodjango/api/data/tl_2015_us_county/tl_2015_us_county.shp'

    def handle(self, *args, **options):
        lm = LayerMapping(Geo, self.shp_file, geo_mapping, transform=False, transaction_mode='commit_on_success', encoding='utf-8')
        lm.save(step=10, progress=1000, strict=False)
