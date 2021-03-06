# ##########################################################
# Created on Sat May 14 2022
# 
# __author__ = Mohit Anand
# __copyright__ = Copyright (c) 2022, CW4F Project
# __credits__ = [Mohit Anand,]
# __license__ = Private
# __version__ = 0.0.0
# __maintainer__ = Mohit Anand
# __email__ = itsmohitanand@gmail.com
# __status__ = Development
# ##########################################################

from datetime import datetime
from cw.cfg import GLOFAS_DIR, EFAS_DIR, CW_DIR
import xarray as xr
import datetime
import pandas as pd

def read_glofas_data(year:int=2021, day:int=1, month:int=1):
    """
    Reads the GLOFAS data for the given year and day.
    """
    file_name = GLOFAS_DIR + 'glofas_' + str(year) + '.grib'

    glofas_dataset = xr.open_dataset(file_name)
    
    return glofas_dataset.get("dis24").sel(time=datetime.datetime(year, month, day))

def read_efas_data(year:int=2021, day:int=1, month:int=1):
    """
    Reads the GLOFAS data for the given year and day.
    """
    file_name = EFAS_DIR + 'efas_' + str(year) + '.grib'
    print(file_name)
    efas_dataset = xr.open_dataset(file_name)
    return efas_dataset.get("dis24").sel(time=datetime.datetime(year, month, day, hour=6))

def read_cw_data():
    """
    Read the crowd water data 
    """

    file_name = CW_DIR + 'export.csv'

    data = pd.read_csv(file_name)

    return data


