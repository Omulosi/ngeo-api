# Generated by Django 2.2.16 on 2021-01-14 08:45

import os
from django.contrib.gis.utils import LayerMapping
from ngeo.apps.shapefiles.models import CountyGazetted

DATA_DIR_NAME = os.path.join("data", "county_gazetted")


# Auto-generated `LayerMapping` dictionary for CountyGazetted model
countygazetted_mapping = {
    'const_nam': 'const_nam',
    'const_no': 'const_no',
    'county_nam': 'county_nam',
    'st_area_sh': 'st_area_sh',
    'st_length_field': 'st_length_',
    'counties': 'COUNTIES',
    'count': 'COUNT',
    'country': 'COUNTRY',
    'area_sqkm': 'AREA_SQKM',
    'color_code': 'color_code',
    'data_colle': 'DATA_COLLE',
    'phase': 'PHASE',
    'geom': 'MULTIPOLYGON',
}


county_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), DATA_DIR_NAME, "county_boundaries.shp")
)


def run(verbose=True):
    """
    This function used the LayerMapping import utility to
    load a shapefile to the database
    """
    # Takes model name, path to shapefile, mapping dict, encoding format
    lm = LayerMapping(
        CountyGazetted, county_shp, countygazetted_mapping, transform=False, encoding="iso-8859-1"
    )
    lm.save(strict=True, verbose=verbose)
