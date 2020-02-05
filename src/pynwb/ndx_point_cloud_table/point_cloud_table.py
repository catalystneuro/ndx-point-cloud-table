from hdmf.common import DynamicTable, register_class, register_map
from hdmf.common.io.table import DynamicTableMap
from hdmf.utils import docval, call_docval_func, get_docval


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
