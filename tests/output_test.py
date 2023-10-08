import pytest
import glob
import datetime

anomes = datetime.date.today().strftime('%Y%m')

param_list = [("output/AERODROMOS/aerodromos_*.snappy.parquet"),
                          ("output/AIR_CIA/air_cia_*.snappy.parquet"),
                          ("output/VRA/vra_*.snappy.parquet")]

@pytest.mark.parametrize('input',
                         param_list)
def test_output(input):
    assert glob.glob(input)