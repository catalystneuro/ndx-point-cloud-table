# ndx-point-cloud-table Extension for NWB

## Installation

```shell script
pip install ndx-point-cloud-table
```

## Usage

```python
from datetime import datetime

from pynwb import NWBFile, NWBHDF5IO
from ndx_point_cloud_table import PointCloudTable

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

point_cloud_table = PointCloudTable(name='test_name', description='description')

point_cloud_table.add_row(point_cloud=[[1., 1., 1.], [2., 2., 2.]], timestamp=.4)

behavior_mod = nwb.create_processing_module('behavior', 'desc')
nwb.processing['behavior'].add(point_cloud_table)

# Write nwb file
with NWBHDF5IO('test_pointcloudtable.nwb', 'w') as io:
    io.write(nwb)

# Read nwb file and check its content
with NWBHDF5IO('test_pointcloudtable.nwb', 'r', load_namespaces=True) as io:
    nwb2 = io.read()
```