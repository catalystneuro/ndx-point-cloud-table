import os

from hdmf.common import DynamicTable, register_class, register_map, load_namespaces
from hdmf.common.io.table import DynamicTableMap


name = 'ndx-point-cloud-table'
# Set path of the namespace.yaml file to the expected install location
ndx_point_cloud_table_specpath = os.path.join(
    os.path.dirname(__file__),
    'spec',
    name + '.namespace.yaml'
)

# If the extension has not been installed yet but we are running directly from
# the git repo
if not os.path.exists(ndx_point_cloud_table_specpath):
    ndx_point_cloud_table_specpath = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', '..',
        'spec',
        name + '.namespace.yaml'
    ))


load_namespaces(ndx_point_cloud_table_specpath)


@register_class('PointCloudTable', 'ndx-point-cloud-table')
class PointCloudTable(DynamicTable):
    """
    Table for storing point cloud data
    """

    __columns__ = (
        {'name': 'point_cloud', 'description': 'datapoints locations over time', 'required': True, 'index': True},
        {'name': 'timestamp', 'description': 'time of each frame in seconds', 'required': True, 'index': False},
        {'name': 'color', 'description': 'datapoints color', 'required': False, 'index': True}
    )


@register_map(PointCloudTable)
class PointCloudTableMap(DynamicTableMap):
    pass


