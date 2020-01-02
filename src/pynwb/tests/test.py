from datetime import datetime
from pynwb import NWBFile, NWBHDF5IO
from hdmf.common.table import VectorIndex, VectorData, DynamicTable
from ndx_point_cloud_table import PointCloudTable

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

data = [[1., 1., 1.], [2., 2., 2.], [1., 2., 1.]]
data_vect = VectorData(name='point_cloud', description='desc', data=data)

indexes = [2, 3]
data_ind = VectorIndex(name='point_cloud_index', data=indexes, target=data_vect)

point_cloud_table = PointCloudTable(name='test_name', description='description')

point_cloud_table.add_row(point_cloud=[[1., 1., 1.], [2., 2., 2.]], timestamp=.4)

behavior_mod = nwb.create_processing_module('behavior', 'desc')
nwb.processing['behavior'].add(point_cloud_table)

print('before write')
print(nwb.processing['behavior'].data_interfaces)

# Write nwb file
with NWBHDF5IO('test_pointcloudtable.nwb', 'w') as io:
    io.write(nwb)

# Read nwb file and check its content
with NWBHDF5IO('test_pointcloudtable.nwb', 'r', load_namespaces=True) as io:
    nwb2 = io.read()
    print('after read')
    print(nwb2.processing['behavior'].data_interfaces)

#os.remove('test_pointcloudtable.nwb')
