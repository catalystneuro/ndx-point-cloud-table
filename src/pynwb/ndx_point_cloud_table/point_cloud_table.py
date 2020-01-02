import os

from hdmf.common import DynamicTable, register_class, register_map, load_namespaces
from hdmf.common.io.table import DynamicTableMap
from hdmf.utils import docval, getargs, popargs, call_docval_func, get_docval

name = 'ndx-point-cloud-table'
# Set path of the namespace.yaml file to the expected install location
ndx_point_cloud_table_specpath = os.path.join(os.path.dirname(__file__), 'spec', name + '.namespace.yaml')

load_namespaces(ndx_point_cloud_table_specpath)


@register_class('PointCloudTable', 'ndx-point-cloud-table')
class PointCloudTable(DynamicTable):
    """
    Table for storing point cloud data
    """

    __columns__ = (
        {'name': 'point_cloud', 'description': 'datapoints locations over time', 'required': True, 'index': True},
        {'name': 'timestamps', 'description': 'time of each frame in seconds', 'required': True, 'index': False},
        {'name': 'color', 'description': 'datapoints color', 'required': False, 'index': True}
    )

    @docval(dict(name='name', type=str, doc='name of this PointCloudTable', default='PointCloudTable'),  # required
            dict(name='description', type=str, doc='Description of this TimeIntervals',
                 default="points from a tracking system"),
            *get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))
    def __init__(self, **kwargs):
        call_docval_func(super(PointCloudTable, self).__init__, kwargs)


@register_map(PointCloudTable)
class PointCloudTableMap(DynamicTableMap):
    pass


