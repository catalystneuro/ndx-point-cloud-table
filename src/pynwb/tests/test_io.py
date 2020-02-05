from datetime import datetime
from ndx_point_cloud_table import PointCloudTable
from pynwb import NWBFile, NWBHDF5IO


def test_io(tmpdir):
    nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

    point_cloud_table = PointCloudTable()

    point_cloud_table.add_row(point_cloud=[[1., 1., 1.], [2., 2., 2.]], timestamps=.4)

    behavior_mod = nwb.create_processing_module('behavior', 'desc')
    nwb.processing[behavior_mod.name].add(point_cloud_table)

    # Write nwb file
    with NWBHDF5IO(str(tmpdir.join('test_pointcloudtable.nwb')), 'w') as io:
        io.write(nwb)

    # Read nwb file and check its content
    with NWBHDF5IO(str(tmpdir.join('test_pointcloudtable.nwb')), 'r', load_namespaces=True) as io:
        io.read()
