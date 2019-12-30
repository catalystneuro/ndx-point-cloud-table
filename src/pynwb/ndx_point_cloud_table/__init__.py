import os
from pynwb import load_namespaces

# Set path of the namespace.yaml file to the expected install location
ndx_point_cloud_table_specpath = os.path.join(
    os.path.dirname(__file__),
    'spec',
    'ndx-point-cloud-table.namespace.yaml'
)

# If the extension has not been installed yet but we are running directly from
# the git repo
if not os.path.exists(ndx_point_cloud_table_specpath):
    ndx_point_cloud_table_specpath = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', '..',
        'spec',
        'ndx-point-cloud-table.namespace.yaml'
    ))

# Load the namespace
load_namespaces(ndx_point_cloud_table_specpath)
